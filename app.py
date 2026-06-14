# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, request, render_template
import sqlite3
import os 

app = Flask(__name__, template_folder='.') # Serves HTML from the same directory

DB_FILE = 'leaderboard.db'

def init_db():
    """Creates the database table if it doesn't exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        ''')
        conn.commit()

@app.route('/')
def home():
    """Serves the main game page."""
    return render_template('index.html')

@app.route('/api/scores', methods=['GET'])
def get_scores():
    """Fetches the top 5 high scores."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, score FROM scores ORDER BY score DESC LIMIT 5')
        top_scores = [{'username': row[0], 'score': row[1]} for row in cursor.fetchall()]
    return jsonify(top_scores)

@app.route('/api/scores', methods=['POST'])
def save_score():
    """Saves a new score sent from the game."""
    data = request.json
    username = data.get('username', 'Anonymous')
    score = data.get('score', 0)
    
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO scores (username, score) VALUES (?, ?)', (username, score))
        conn.commit()
        
    return jsonify({"status": "success", "message": "Score saved!"}), 201


# CRITICAL FIX: Run this out in the open so Gunicorn executes it on Render startup!
init_db()

if __name__ == '__main__':
    # Gets the port from the cloud provider, defaults to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)