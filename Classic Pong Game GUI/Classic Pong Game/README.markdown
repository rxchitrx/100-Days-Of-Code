# Classic Pong Game - Day 22 Project

## Overview
This project is an implementation of the classic Pong arcade game using Python and the Turtle module. Pong is a two-dimensional sports game that simulates table tennis. Players control paddles to hit a ball back and forth across the screen, with the objective of scoring points by getting the ball past the opponent's paddle.

## Features
- Two-player gameplay with left and right paddles.
- Real-time ball movement and collision detection.
- Score tracking for both players.
- Simple and intuitive controls using keyboard inputs.
- Responsive game reset after scoring.

## Requirements
- Python 3.x
- Turtle module (included with standard Python library)

## Installation
1. Ensure Python 3.x is installed on your system.
2. Clone or download the project files.
3. No additional installation is required as the Turtle module is part of the Python standard library.

## File Structure
- `main.py`: The main game logic and setup.
- `ball.py`: Defines the Ball class for ball movement and behavior.
- `paddle.py`: Defines the Paddle class for paddle movement.
- `scoreboard.py`: Handles the score display and updates.

## How to Play
1. Run `main.py` to start the game.
2. Use the following keys to control the paddles:
   - Left Paddle: "w" (up), "s" (down)
   - Right Paddle: "Up Arrow" (up), "Down Arrow" (down)
3. Hit the ball with your paddle to keep it in play.
4. Score a point when the ball passes the opponent's paddle.
5. The game continues until manually stopped.

## Code Breakdown
### `main.py`
- Initializes the game screen and sets up the paddles, ball, and scoreboard.
- Handles the game loop, including ball movement, collision detection, and score updates.
- Listens for keyboard inputs to control paddle movement.

### `ball.py`
- Defines the `Ball` class with methods for movement, wall bounce, paddle bounce, and resetting position.
- Manages the ball's speed and direction.

### `paddle.py`
- Defines the `Paddle` class with methods for moving up and down.
- Controls the paddle's position on the screen.

### `scoreboard.py`
- Defines the `ScoreBoard` class to display and update the score for both players.
- Updates the scoreboard in real-time as points are scored.

## Controls
- **Left Paddle**: 
  - "w" key: Move up
  - "s" key: Move down
- **Right Paddle**: 
  - Up Arrow: Move up
  - Down Arrow: Move down

## Game Rules
- The ball moves across the screen, bouncing off the top and bottom walls.
- Players must hit the ball with their paddle to prevent it from passing.
- A point is scored when the ball passes a paddle.
- The game resets the ball position after a point is scored.

## Contributing
Feel free to fork this repository and submit pull requests for enhancements or bug fixes. Suggestions for new features are welcome!

## License
This project is open-source and available under the MIT License.

## Acknowledgements
- Inspired by the classic Pong game by Atari.
- Built using the Turtle module from the Python standard library.