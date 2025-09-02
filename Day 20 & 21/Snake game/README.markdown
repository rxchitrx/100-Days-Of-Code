# Snake Game Project

## Overview
This Folder contains a classic Snake game implementation using Python and the Turtle module. The game is a recreation of the nostalgic arcade game where a snake grows longer as it eats food, with the objective of avoiding collisions with the walls and itself.

## Features
- Classic snake movement using keys (w, a, s, d).
- Score tracking with a scoreboard that increments when food is consumed.
- Game over condition when the snake hits the wall or itself.
- Random food spawning within the game boundaries.

## Files
- `main.py`: The main game logic and setup.
- `snake.py`: Contains the `Snake` class for managing the snake's movement and growth.
- `food.py`: Defines the `Food` class for random food placement.
- `scoreboard.py`: Implements the `Scoreboard` class for tracking and displaying the score.

## How to Run
1. Ensure you have Python installed on your system (version 3.6 or higher recommended).
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/rxchitrx/100-Days-Of-Code.git
   ```
3. Navigate to the project directory:
   ```bash
   cd snake-game
   ```
4. Run the game:
   ```bash
   python main.py
   ```

## Controls
- **W key**: Move the snake up.
- **S key**: Move the snake down.
- **A key**: Move the snake left.
- **D key**: Move the snake right.

## Game Rules
- Use the arrow keys to control the snake's direction.
- Eat the food (blue circle) to grow longer and increase your score.
- Avoid hitting the walls or the snake's own body to stay alive.
- The game ends if the snake collides with the boundary or itself.

## Acknowledgements
- Inspired by the classic Snake game from older mobile phones and arcade machines.
- Utilizes the Python Turtle module for simple graphics and game development.