# WackAMole

A modern, interactive, and visually stunning web-based Whack-a-Mole game featuring a sleek user interface, smooth micro-animations, and a Python-powered backend leaderboard system.

---

## Features

- **Dynamic Gameplay**: Fast-paced, classic Whack-a-Mole experience with randomized mole appearances, speed scaling, and interactive animations.
- **Modern UI/UX**: Premium aesthetics with curated glassmorphism styling, a dark mode color palette, smooth transitions, and responsive design for all screen sizes.
- **Score Tracking**: Real-time score counting, combo indicators, and a persistent leaderboard system.
- **Python Backend**: A lightweight Python backend (`app.py`) for managing high scores, handling API requests for the leaderboard, and storing scores securely.
- **Audio Feedback**: Immersive sound effects for whack hits, misses, and game-over states (customizable/toggleable).

---

## Technology Stack

- **Frontend**:
  - HTML5 (Semantic structure)
  - Vanilla CSS3 (Custom variables, modern layout, animations)
  - JavaScript (ES6+, DOM manipulation, game loop logic)
- **Backend**:
  - Python 3 (Flask or FastAPI)
  - SQLite (Lightweight database for leaderboard data persistence)

---

## 📁 Project Structure

```text
WackAMole/
├── app.py             # Python backend server (API & database handlers)
├── index.html         # Frontend game interface & scripts
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation (this file)
```

---

##  Getting Started

### Prerequisites

- A modern web browser.
- **Python 3.x** (optional, required only if running the leaderboard backend).

### Setup and Running

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sharr-catalyst/WackAMole.git
   cd WackAMole
   ```

2. **Run the Frontend (Directly)**:
   - Simply double-click `index.html` or use a local development server extension (e.g., Live Server in VS Code) to launch the game interface.

3. **Run the Backend (Leaderboard API)**:
   - Create a virtual environment and install requirements (e.g., Flask):
     ```bash
     python -m venv venv
     ./venv/Scripts/activate # Windows
     pip install Flask
     ```
   - Start the backend server:
     ```bash
     python app.py
     ```
   - Open `index.html` in your browser. The game will automatically detect and sync high scores with the running local server.

---

## 🎮 How to Play

1. Click **Start Game** to initiate the timer.
2. Moles will randomly pop out of the dirt mounds.
3. Click (or tap) on the mole before it retreats back into its hole.
4. Each successful whack awards you points. Avoid hitting empty mounds, as it might deduct points or break your combo multiplier!
5. Try to achieve the highest score before the timer runs out and secure your spot on the leaderboard!

---

## 🎨 License

This project is open-source and available under the [MIT License](LICENSE).
