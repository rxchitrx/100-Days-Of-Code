# Password Manager Application

## Overview
This is a simple Password Manager application built using Python and the `tkinter` library. It allows users to generate random passwords and save them along with website and username/email details to a text file. The application includes a user-friendly interface with features to generate secure passwords and store them securely.

## Features
- **Password Generation**: Generates a random password using a combination of letters, numbers, and symbols.
- **Password Copy**: Automatically copies the generated password to the clipboard.
- **Data Storage**: Saves website, username/email, and password details to a `data.txt` file.
- **Input Validation**: Checks for empty fields and prompts the user to confirm before saving data.
- **User Interface**: Provides a clean GUI with labeled entry fields and buttons.

## Prerequisites
- Python 3.x
- Required libraries:
  - `tkinter` (usually included with Python)
  - `pyperclip` (for copying to clipboard)

To install the required library, run the following command:
```bash
pip install pyperclip
```

## Usage
1. **Run the Application**:
   - Ensure all prerequisites are installed.
   - Place the `logo.png` file in the same directory as the script (required for the GUI logo).
   - Execute the script:
     ```bash
     python password_manager.py
     ```

2. **Interface Overview**:
   - **Website**: Enter the website name for which the password is being generated.
   - **Email/Username**: Enter the email or username (default pre-filled with "rachitmital@gmail.com").
   - **Password**: Click the "Generate" button to create a random password, which will be auto-filled and copied to the clipboard.
   - **Add**: Click the "Add" button to save the entered details after confirmation.

3. **Saving Data**:
   - The application will prompt a warning if any field is empty.
   - Upon confirmation, the details are appended to `data.txt` in the format: `website | username | password`.
   - After saving, the website and password fields are cleared.

## Code Structure
- **Imports**: 
  - `tkinter` for GUI.
  - `messagebox` for dialog boxes.
  - `random` for password generation.
  - `pyperclip` for copying to clipboard.
- **Functions**:
  - `generate_password()`: Generates and inserts a random password.
  - `save_info()`: Validates and saves the input data to a file.
- **UI Setup**: Configures the main window, canvas, labels, entry fields, and buttons.

## File Details
- **logo.png**: An image file used as the application logo (must be in the same directory).
- **data.txt**: A text file where password data is stored (created automatically if it doesn't exist).

## Customization
- **Password Complexity**: Modify the `letters`, `numbers`, and `symbols` lists in `generate_password()` to change the character sets.
- **Default Username**: Update the `user_entry.insert(0, "rachitmital@gmail.com")` line to set a different default email/username.
- **File Path**: Change the `"data.txt"` file name or path in `save_info()` to store data elsewhere.

## Limitations
- The application stores passwords in plain text in `data.txt`, which is not secure for real-world use. For production, consider encrypting the data.
- The `logo.png` file is required; the application will fail if it's missing.
- No data retrieval or editing functionality is implemented.

## Contributing
Feel free to fork this repository and submit pull requests for enhancements, such as:
- Adding encryption for stored passwords.
- Implementing data retrieval and editing features.
- Enhancing the UI with additional styling or validation.

## License
This project is open-source and available under the MIT License.

## Contact
For questions or support, please open an issue on the repository or contact the maintainer.