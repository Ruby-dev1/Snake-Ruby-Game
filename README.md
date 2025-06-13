# 🐍 Snake Game (Pygame)

A beginner-friendly **Snake Game** built using Python and Pygame.  
This project is inspired by the classic snake game where the snake eats food, grows longer, and avoids crashing too many times.

---

## 🎮 Features

- ✅ Smooth keyboard controls (arrow keys)
- 🍎 Multiple food items appear randomly
- 🐍 Snake grows longer as it eats
- 🧱 Bounces from walls (maximum 3 allowed)
- 🎉 Win condition: Reach a certain length
- 😵 Game Over when bounce limit is reached
- 🔁 Restart the game using `R` key

---

## 🧰 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Game
bash
Copy
Edit
python snake_game.py
⌨️ Controls
Arrow Keys — Move the snake

R — Restart after game over

📸 Screenshots
Gameplay:

Game Over Screen:

🗂️ Project Structure
bash
Copy
Edit
snake-game/
├── snake_game.py         # Main game logic
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignoring cache files
├── Game 1.JPG            # Gameplay screenshot
└── game 3.JPG            # Game over screenshot
🧠 How It Works (Quick Summary)
The game uses Pygame to create a grid-based canvas.

Snake moves continuously based on the last arrow key press.

On hitting the walls, it bounces back (max 3 times).

When the snake eats food, it grows longer.

If the snake reaches a certain length (15 blocks), you win.

If the snake hits walls more than 3 times — Game Over!

✅ Todo (Optional Enhancements)
Add sound effects 🎵

Add high-score system 🏆

Add levels or speed increase ⏩

Add background graphics 🎨

🤝 Contributing
Pull requests and stars are always welcome!

🧑‍💻 Author
Made with ❤️ by Rubina



