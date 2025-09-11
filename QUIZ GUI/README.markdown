# Quizzler Application

## Overview

This is a Quizzler application built using Python, designed as an interactive quiz game. The project fetches true/false questions from the Open Trivia Database API and presents them through a graphical user interface (GUI) created with the `tkinter` library. The application tracks the user's score, provides feedback on answers, and ends when all questions are answered. This project is part of a learning exercise, showcasing object-oriented programming and API integration.

## Features

- **Question Fetching**: Retrieves 10 true/false questions from the Open Trivia Database API.
- **Interactive GUI**: Displays questions and score on a canvas with "True" and "False" buttons.
- **Answer Feedback**: Changes the canvas background to green for correct answers or red for incorrect ones, with a 1-second delay before the next question.
- **Score Tracking**: Updates and displays the user's score in real-time.
- **End of Quiz**: Disables buttons and shows a completion message when all questions are answered.

## Prerequisites

- Python 3.x
- Required libraries:
  - `tkinter` (included with Python)
  - `requests` (for API calls)

Install the required library using:

```bash
pip install requests
```

## Usage

1. **Set Up the Environment**:

   - Install the `requests` library as described above.
   - Ensure the image files `true.png` and `false.png` are placed in the `Quiz Game/images/` directory relative to the script.

2. **Run the Application**:

   - Execute the script from the terminal in the project directory:

     ```bash
     python main.py
     ```

3. **Gameplay**:

   - The GUI will display a question on the canvas.
   - Click the "True" or "False" button to answer.
   - The canvas will turn green for a correct answer or red for an incorrect one, then move to the next question after 1 second.
   - The game ends when all 10 questions are answered, showing the final score.

## Code Structure

- **main.py**: Entry point of the application.
  - Initializes a `Question` bank from `question_data`.
  - Creates a `QuizBrain` instance and a `QuizInterface` to run the quiz.
- **data.py**: Fetches question data from the Open Trivia Database API.
- **question_model.py**: Defines the `Question` class to store question text and answer.
- **quiz_brain.py**: Manages the quiz logic, including question progression and answer checking.
- **ui.py**: Implements the GUI with `tkinter`, handling question display, button interactions, and feedback.

## File Details

- **true.png** and **false.png**: Image files for the "True" and "False" buttons, located in `Quiz Game/images/`.
- **data.json**: Not used directly; questions are fetched from the API.

## Customization

- **Question Count**: Modify the `amount=10` parameter in the API URL in `data.py` to change the number of questions.
- **Theme Color**: Adjust `THEME_COLOR` in `ui.py` to change the background color.
- **Images**: Replace `true.png` and `false.png` with custom images of the same name and format (PNG) in the `Quiz GUI/images/` directory.

## Limitations

- **Internet Dependency**: Requires an active internet connection to fetch questions from the API.
- **Image Requirement**: The script fails if `true.png` or `false.png` are missing or invalid.
- **No Persistence**: Scores and progress are not saved between sessions.
- **Fixed Question Type**: Only supports true/false questions due to the API parameter `type=boolean`.

## License

This project is open-source under the MIT License.