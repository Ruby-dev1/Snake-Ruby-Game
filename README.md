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
https://github.com/Ruby-dev1/Snake-Ruby-Game/
cd Snake-Ruby-Game
2. Install Dependencies
pip install pygame
3. Run the Game
python main.py
⌨️ Controls
Arrow Keys — Move the snake

R — Restart after game over

🗂️ Project Structure
snake-game/
├── main.py         # Main game logic
├── README.md             # Project documentation
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



