# Workout Tracker

## Overview
The Workout Tracker is a Python-based application designed to log and track workout data, integrating with external APIs to manage exercise routines and nutritional information. This project combines data from Sheety API for workout logging and Nutritionix API for exercise and calorie tracking.

## Features
- Log workout details including date, time, exercise type, duration, and calories burned.
- Fetch exercise data and nutritional information via Nutritionix API.
- Store workout data using Sheety API.
- Real-time data processing with user input for personalized tracking.

## Installation

### Prerequisites
- Python 3.x
- Required Python packages: `requests`, `os`, `dotenv`, `datetime`

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd workout-tracker
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your API keys:
   ```
   SHEETY_API_ENDPOINT=your_sheety_api_endpoint
   SHEETY_TOKEN=your_sheety_token
   NUTRITIONIX_APP_ID=your_nutritionix_app_id
   NUTRITIONIX_API_KEY=your_nutritionix_api_key
   ```

## Usage
1. Run the `main.py` script:
   ```bash
   python main.py
   ```
2. Follow the prompts to input your workout details or exercise query.
3. The script will process the input, fetch relevant data, and log it to the Sheety API.

## Project Structure
- `Sheety.py`: Contains the `sheety` class for handling workout data logging.
- `nutritionix.py`: Contains the `nutrition` class for fetching exercise and nutritional data.
- `main.py`: Main script to orchestrate the application flow.
- `.env`: Environment file for storing API credentials.

## Classes and Methods

### `sheety` Class (Sheety.py)
- `__init__(self, date, time, Exercise, Duration, Calories)`: Initializes a workout entry with provided details and API credentials.
- Logs the workout data to the Sheety API endpoint.

### `nutrition` Class (nutritionix.py)
- `__init__(self)`: Initializes with Nutritionix API credentials and base URL.
- Fetches exercise data based on user input (e.g., query, weight, height, age).

### `main.py`
- Orchestrates the flow by creating instances of `nutrition` and `sheety` classes.
- Handles date-time generation and data transfer between APIs.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
For any questions or suggestions, please open an issue on the repository or contact the maintainer.