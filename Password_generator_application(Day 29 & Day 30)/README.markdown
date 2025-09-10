# Password Manager Application

## Overview

This is an updated Password Manager application built as part of the **Day 30** challenge of the "100 Days of Code" course by Angela Yu. This version enhances the previous **Day 29** implementation by introducing JSON-based data storage, a search functionality to retrieve saved passwords, and an improved user interface. The application is built using Python with the `tkinter` library for the GUI.

## Features

- **Password Generation**: Generates a random password using a combination of letters, numbers, and symbols.
- **Data Storage**: Saves website, email/username, and password details to a `data.json` file in a structured JSON format.
- **Search Functionality**: Allows users to search for and retrieve saved password details for a specific website.
- **Input Validation**: Ensures no fields are left empty before saving data.
- **User Interface**: Features a clean GUI with a logo, labeled entry fields, and interactive buttons.

## Prerequisites

- Python 3.x
- Required libraries:
  - `tkinter` (included with Python)

No additional libraries are required for this version, as it relies solely on standard Python modules and `tkinter`.

## Usage

1. **Run the Application**:

   - Ensure all prerequisites are met.
   - Place the `logo.png` file in the same directory as the script.
   - Execute the script:

     ```bash
     python password_manager.py
     ```

2. **Interface Overview**:

   - **Website**: Enter the website name for the password.
   - **Email/Username**: Enter the email or username (default pre-filled with "angela@gmail.com").
   - **Password**: Click "Generate Password" to create a random password, which auto-fills the field.
   - **Add**: Click "Add" to save the details to `data.json` after validation.
   - **Search**: Click "Search" to retrieve saved password details for the entered website.

3. **Saving Data**:

   - A warning appears if the website or password field is empty.
   - Upon confirmation, details are saved to `data.json` with proper indentation.
   - Website and password fields are cleared after saving.

4. **Searching Data**:

   - Enter a website name and click "Search" to view the associated email and password.
   - Displays a warning if no data exists or if the website is not found.

## Code Structure

- **Imports**:
  - `tkinter` for GUI.
  - `messagebox` for dialog boxes.
  - `random` for password generation.
  - `json` for data storage and retrieval.
- **Functions**:
  - `generate_password()`: Generates and inserts a random password.
  - `search()`: Retrieves and displays saved password details for a website.
  - `save()`: Validates and saves input data to `data.json`.
- **UI Setup**: Configures the window, canvas with logo, labels, entries, and buttons.

## File Details

- **logo.png**: An image file used as the application logo (must be in the project directory).
- **data.json**: A JSON file for storing password data (created if absent).

## Customization

- **Password Complexity**: Modify the `letters`, `numbers`, and `symbols` lists in `generate_password()` to adjust character sets.
- **Default Username**: Change the `email_entry.insert(0, "angela@gmail.com")` line for a different default.
- **File Path**: Update the `"data.json"` path in `save()` to store data elsewhere.

## Limitations

- Passwords are stored in plain text in `data.json`, unsuitable for real-world use without encryption.
- Requires `logo.png`; the app fails if missing or invalid.
- No data editing or deletion features.

## 