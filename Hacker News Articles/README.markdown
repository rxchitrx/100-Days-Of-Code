# Hacker News Top Stories WhatsApp Notifier

This project is a Python script that scrapes the top five highest-scored articles from the Hacker News website (https://news.ycombinator.com/) and sends their titles, scores, and links as a formatted message to a specified phone number via WhatsApp using the Twilio API.

## Table of Contents

- Overview
- Features
- Prerequisites
- Setup Instructions
- Usage
- Code Explanation
- Dependencies
- Security Notes
- Troubleshooting
- Contributing
- License

## Overview

The script fetches the latest articles from Hacker News, extracts the titles, links, and scores, sorts them by score in descending order, and sends the top five articles as a WhatsApp message. It uses the `requests` library for web scraping, `BeautifulSoup` for HTML parsing, and the `twilio` library to send messages via WhatsApp.

## Features

- Scrapes article titles, links, and scores from Hacker News.
- Sorts articles by score and selects the top five.
- Sends a formatted WhatsApp message with the top articles to a specified phone number.
- Easy to configure with Twilio credentials and phone numbers.

## Prerequisites

To run this script, you need:

- Python 3.6 or higher installed.
- A Twilio account with WhatsApp messaging enabled.
- A Twilio phone number capable of sending WhatsApp messages.
- A personal phone number registered with WhatsApp to receive messages.

## Setup Instructions

1. **Install Python Dependencies**: Install the required Python libraries using pip:

   ```bash
   pip install requests beautifulsoup4 twilio
   ```

2. **Set Up Twilio Account**:

   - Sign up for a Twilio account at https://www.twilio.com/.
   - Obtain your **Account SID** and **Auth Token** from the Twilio Console.
   - Purchase or configure a Twilio phone number that supports WhatsApp messaging.
   - Enable WhatsApp for your Twilio number by following Twilio's documentation: https://www.twilio.com/docs/whatsapp.

3. **Configure Environment Variables**: To securely handle sensitive information, store your Twilio credentials and phone numbers as environment variables:

   - On Windows (Command Prompt):

     ```bash
     set TWILIO_ACCOUNT_SID=your_account_sid
     set TWILIO_AUTH_TOKEN=your_auth_token
     set TWILIO_NUMBER=your_twilio_whatsapp_number
     set PERSONAL_NUMBER=your_personal_whatsapp_number
     ```
   - On macOS/Linux:

     ```bash
     export TWILIO_ACCOUNT_SID=your_account_sid
     export TWILIO_AUTH_TOKEN=your_auth_token
     export TWILIO_NUMBER=your_twilio_whatsapp_number
     export PERSONAL_NUMBER=your_personal_whatsapp_number
     ```

   Alternatively, you can hardcode these values in the script (not recommended for security reasons).

4. **Update the Script**: Replace the placeholder values in the script (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_NUMBER`, `PERSONAL_NUMBER`) with your actual Twilio credentials and phone numbers. For example:

   ```python
   account_sid = "your_actual_account_sid"
   auth_token = "your_actual_auth_token"
   from_="whatsapp:+1234567890"
   to="whatsapp:+0987654321"
   ```

## Usage

1. Run the script:

   ```bash
   python main.py
   ```
2. The script will:
   - Fetch the latest articles from Hacker News.
   - Extract and sort the top five articles by score.
   - Send a WhatsApp message to the specified number with the formatted list of articles.

Example output message sent to WhatsApp:

```
1. Article Title 1 (150 points) : https://example.com
2. Article Title 2 (120 points) : https://example.org
3. Article Title 3 (100 points) : https://example.net
4. Article Title 4 (80 points) : https://example.edu
5. Article Title 5 (60 points) : https://example.gov
```

## Code Explanation

The script performs the following steps:

1. **Imports**:

   - `requests`: To make HTTP requests to the Hacker News website.
   - `BeautifulSoup` (from `bs4`): To parse the HTML content of the webpage.
   - `Client` (from `twilio.rest`): To interact with the Twilio API for sending WhatsApp messages.

2. **Web Scraping**:

   - Sends a GET request to `https://news.ycombinator.com/` to fetch the webpage content.
   - Uses `BeautifulSoup` to parse the HTML and extract all `<span>` elements with the class `titleline`.
   - For each article, extracts the title and link from the nested `<a>` tag.
   - Extracts scores from `<span>` elements with the class `score`, converts them to integers, and sorts them in descending order.

3. **Data Processing**:

   - Combines the top five scores with their corresponding titles and links using `zip`.
   - Formats the data into a list of strings, each representing an article with its rank, title, score, and link.

4. **Sending WhatsApp Message**:

   - Initializes a Twilio `Client` with the provided Account SID and Auth Token.
   - Creates a WhatsApp message with the formatted article list and sends it from the Twilio number to the personal number.

## Dependencies

- `requests` (&gt;=2.28.0): For making HTTP requests.
- `beautifulsoup4` (&gt;=4.10.0): For HTML parsing.
- `twilio` (&gt;=7.0.0): For sending WhatsApp messages via the Twilio API.

Install dependencies using:

```bash
pip install requests beautifulsoup4 twilio
```

## Security Notes

- **Sensitive Information**: Avoid hardcoding Twilio credentials (`account_sid`, `auth_token`) or phone numbers in the script. Use environment variables or a secure configuration file to store them.
- **Rate Limits**: Be aware of Twilio's messaging rate limits and Hacker News's scraping policies. Excessive requests to Hacker News may lead to IP blocking.
- **WhatsApp Policies**: Ensure the recipient has opted in to receive WhatsApp messages, as per Twilio and WhatsApp's terms of service.

## Troubleshooting

- **Twilio Errors**:
  - **Invalid Credentials**: Verify your Account SID and Auth Token in the Twilio Console.
  - **WhatsApp Not Enabled**: Ensure your Twilio number is configured for WhatsApp messaging.
  - **Invalid Phone Number**: Ensure both `from_` and `to` numbers are in the correct format (`whatsapp:+[country_code][number]`).
- **Scraping Issues**:
  - **Empty Titles or Links**: Check if Hacker News's HTML structure has changed. Inspect the webpage and update the `soup.find_all` selectors if needed.
  - **HTTP Errors**: Ensure a stable internet connection. If `requests.get` fails, handle exceptions using a `try-except` block.
- **Message Not Received**: Verify the recipient's phone number is registered with WhatsApp and that the Twilio number is correctly configured.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.