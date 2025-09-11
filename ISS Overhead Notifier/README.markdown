# ISS Overhead Notification System

## Overview

This is a Python script designed to notify you when the International Space Station (ISS) is overhead, provided it is nighttime at your location. The script uses the Open Notify API to track the ISS's current position and the Sunrise-Sunset API to determine sunrise and sunset times. It sends an email alert using SMTP when the ISS is within a specified geographic range and it is dark outside. This project is suitable for astronomy enthusiasts or anyone interested in tracking the ISS.

## Features

- **ISS Position Tracking**: Fetches real-time latitude and longitude of the ISS using the Open Notify API.
- **Sunrise/Sunset Calculation**: Determines local sunrise and sunset times based on your latitude and longitude using the Sunrise-Sunset API.
- **Nighttime Detection**: Checks if it is dark at your location by comparing the current time with sunrise and sunset times.
- **Email Notification**: Sends an email alert when the ISS is overhead and it is nighttime.
- **Continuous Monitoring**: Runs in a loop, checking conditions every 60 seconds.

## Prerequisites

- Python 3.x
- Required libraries:
  - `requests` (for API calls)
  - `smtplib` (for email sending, included with Python)
  - `datetime` (included with Python)
  - `time` (included with Python)

Install the required library using:

```bash
pip install requests
```

## Configuration

Before running the script, you must configure the following variables:

- `MY_LAT`: Replace `"your lat here (in float)"` with your latitude as a float (e.g., `51.5074` for London).
- `MY_LONG`: Replace `"Your long here (in float)"` with your longitude as a float (e.g., `-0.1278` for London).
- `my_email`: Replace `"your-email-here"` with your Gmail address.
- `password`: Replace `"app-password-generated-from-google-account-settings"` with an App Password generated from your Google Account settings (required for SMTP with 2FA enabled).
- `to_addrs`: Replace `"email-to-send-to"` with the email address to receive notifications.

### Notes on Configuration

- **Google App Password**: If you use two-factor authentication (2FA) on your Gmail account, you need to generate an App Password in your Google Account settings under "Security" &gt; "App Passwords". Use this 16-character code instead of your regular password.
- **Geographic Range**: The script currently checks if the ISS is within 20° to 30° latitude and 45° to 55° longitude. Adjust these ranges in `iss_close_to_me()` so that they are + or - 5 degrees from your coordinates.

## Usage

1. **Set Up the Environment**:

   - Install the `requests` library as described above.
   - Update the configuration variables with your personal details.

2. **Run the Script**:

   - Execute the script from the terminal:

     ```bash
     python iss_tracker.py
     ```
   - The script will run continuously, printing "Running script..." every 60 seconds and sending an email if conditions are met.

3. **Monitoring**:

   - The script checks every minute if the ISS is within the specified range and if it is dark.
   - An email with the message "Look up the ISS is overhead" will be sent to the configured recipient if both conditions are true.

## Code Structure

- **Imports**:
  - `requests` for API requests.
  - `datetime` for current time handling.
  - `smtplib` for email sending.
  - `time` for sleep functionality.
- **Functions**:
  - `iss_close_to_me()`: Checks if the ISS is within the defined geographic range.
  - `is_dark()`: Determines if it is nighttime based on sunrise and sunset times (note: current implementation has a logic error—see Limitations).
- **Main Logic**:
  - Fetches ISS position and sunrise/sunset data.
  - Runs an infinite loop to monitor conditions and send emails.

## Customization

- **Geographic Range**: Modify the latitude and longitude ranges in `iss_close_to_me()` to match your location.
- **Email Settings**: Adjust the SMTP server or email provider by changing the `smtplib.SMTP("smtp.gmail.com")` line if using a different service.
- **Notification Interval**: Change the `time.sleep(60)` value to adjust how often the script checks (in seconds).

## Limitations

- **Nighttime Logic Error**: The `is_dark()` function currently has a logical error (`if time_now.hour < sunrise_time and time_now.hour > sunset_time`). It should be `if time_now.hour >= sunset_time or time_now.hour < sunrise_time` to correctly identify nighttime (assuming 24-hour format and times are in local hours).
- **Hardcoded Ranges**: The ISS proximity check (20°-30° latitude, 45°-55° longitude) is hardcoded and may not suit all locations.
- **Email Security**: Uses plain text passwords; for production, consider OAuth or more secure authentication methods.
- **No Error Handling for API Downtime**: The script may fail if the Open Notify or Sunrise-Sunset APIs are unavailable.

## License

This project is open-source under the MIT License.

## 