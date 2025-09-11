# U.S. States Game

## Overview

The U.S. States Game is an interactive quiz application built using Python's `turtle` module and `pandas` library. Inspired by Sporcle's U.S. States quiz, the game challenges players to name as many of the 50 U.S. states as possible. Players type state names, and if correct, the state name is written on a blank U.S. map at its corresponding location. The game tracks progress and allows players to exit early, generating a CSV file of states they missed for educational purposes.

## Features

- **Interactive Map**: Displays a blank U.S. map (`blank_states_img.gif`) as the game background.
- **User Input**: Prompts players to enter state names via a pop-up text input box.
- **Dynamic Labeling**: Correctly guessed states are written on the map at their respective coordinates.
- **Progress Tracking**: Displays the number of correctly guessed states (e.g., "5/50 states correct") in the input box title.
- **Case Insensitivity**: Accepts state names regardless of capitalization (e.g., "california", "CALIFORNIA", or "California").
- **Exit Functionality**: Players can type "exit" to end the game early.
- **Learning Tool**: On exit, generates a `states_to_learn.csv` file listing all unguessed states.
- **Data-Driven**: Uses `50_states.csv` containing state names and their x, y coordinates for accurate placement.

## Prerequisites

- **Python**: Version 3.x
- **Libraries**:
  - `turtle` (built-in with Python)
  - `pandas` (install via `pip install pandas`)
- **Files**:
  - `50_states.csv`: Contains state names and their x, y coordinates.
  - `blank_states_img.gif`: A blank U.S. map image in GIF format (required by `turtle`).

## Setup

1. **Download the Project**:

   - Fork the project from the provided repository (see course resources).
   - Download the project as a ZIP file and rename it to `us-states-game` if necessary.
   - Extract the ZIP to your working directory.

2. **Project Structure**:

   ```
   us-states-game/
   ├── main.py
   ├── 50_states.csv
   ├── blank_states_img.gif
   ```

3. **Install Dependencies**:

   - Ensure `pandas` is installed. If not, run:

     ```bash
     pip install pandas
     ```

4. **Open in IDE**:

   - Open the project in an IDE like PyCharm.
   - Ensure `main.py`, `50_states.csv`, and `blank_states_img.gif` are in the same directory.

## How to Play

1. Run `main.py`.
2. A window opens displaying a blank U.S. map.
3. A pop-up prompts you to "Guess the State" with a progress indicator (e.g., "0/50 states correct").
4. Type a state name (case-insensitive, e.g., "california" or "California").
5. If correct:
   - The state name appears on the map at its designated coordinates.
   - The progress counter updates (e.g., "1/50 states correct").
6. If incorrect, the input box reappears for another guess.
7. Continue until all 50 states are guessed or type "exit" to quit.
8. On exit, a `states_to_learn.csv` file is generated, listing all unguessed states.

## Code Explanation

The game is implemented in `main.py` and relies on the following components:

### 1. **Setup Turtle Screen**

- Imports the `turtle` module to create a graphical interface.
- Creates a `turtle.Screen()` object and sets the title to "U.S. States Game".
- Loads `blank_states_img.gif` as a custom shape for the turtle screen background:

  ```python
  screen = turtle.Screen()
  screen.title("U.S. States Game")
  image = "blank_states_img.gif"
  screen.addshape(image)
  turtle.shape(image)
  ```

### 2. **Reading CSV Data**

- Uses `pandas` to read `50_states.csv`, which contains:
  - `state`: State name (title case, e.g., "California").
  - `x`: X-coordinate for state label placement.
  - `y`: Y-coordinate for state label placement.
- Converts the `state` column to a list for membership checking:

  ```python
  import pandas
  data = pandas.read_csv("50_states.csv")
  all_states = data.state.to_list()
  ```

### 3. **Game Loop**

- Initializes an empty list `guessed_states` to track correct guesses.
- Runs a `while` loop until all 50 states are guessed (`len(guessed_states) < 50`):

  ```python
  guessed_states = []
  while len(guessed_states) < 50:
      answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Guess the State").title()
  ```
- Converts user input to title case (`.title()`) for case-insensitive matching.

### 4. **State Validation and Labeling**

- Checks if the user's input (`answer_state`) is in `all_states`.
- If valid:
  - Retrieves the corresponding row from the CSV using `data[data.state == answer_state]`.
  - Creates a turtle to write the state name at the specified x, y coordinates:

    ```python
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)
    ```
- Uses `item()` to extract single values from pandas series (avoids type mismatch errors).

### 5. **Exit and CSV Generation**

- If the user types "Exit", the loop breaks:

  ```python
  if answer_state == "Exit":
      break
  ```
- Generates a list of missing states by comparing `all_states` with `guessed_states`:

  ```python
  missing_states = [state for state in all_states if state not in guessed_states]
  ```
- Creates a new DataFrame and saves it as `states_to_learn.csv`:

  ```python
  new_data = pandas.DataFrame(missing_states)
  new_data.to_csv("states_to_learn.csv")
  ```

### 6. **Error Handling**

- Ensures the image file path matches exactly (`blank_states_img.gif`) to avoid "no such file" errors.
- Converts `x` and `y` coordinates to integers using `int(state_data.x.item())` to prevent type mismatch errors in `turtle`.