# Stock Market News and Price Change Notifier

## Project Overview
This Python script monitors daily stock price changes for a predefined list of major companies and sends WhatsApp notifications with the percentage change and recent news articles related to each company. It integrates with the [Alpha Vantage API](https://www.alphavantage.co) for stock data, [NewsAPI](https://newsapi.org) for news articles, and [Twilio](https://www.twilio.com) for sending WhatsApp messages.

## Features
- Retrieves daily stock price data for major companies (e.g., Apple, Microsoft, Tesla).
- Calculates the percentage change in stock price from the previous day's close to the current day's open.
- Fetches the top three recent news articles for each company.
- Sends a WhatsApp message via Twilio with the stock price change and news summaries.
- Handles errors gracefully (e.g., missing stock data).
- Uses emojis to indicate stock price increase (🔺) or decrease (🔻).

## Prerequisites
To run this script, you need the following:
- Python 3.6 or higher
- API keys and accounts for:
  - [Alpha Vantage](https://www.alphavantage.co) (for stock data)
  - [NewsAPI](https://newsapi.org) (for news articles)
  - [Twilio](https://www.twilio.com) (for WhatsApp messaging)
- A WhatsApp-enabled Twilio number and a destination WhatsApp number

## Installation
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd stock-market-notifier
   ```

2. **Install Required Python Packages**:
   Install the necessary dependencies using pip:
   ```bash
   pip install requests newsapi-python twilio
   ```

3. **Set Up API Keys and Credentials**:
   Replace the placeholder values in the script with your actual credentials:
   - `STOCK_DATA_API_KEY`: Your [Alpha Vantage](https://www.alphavantage.co) API key.
   - `NEWS_API_KEY`: Your [NewsAPI](https://newsapi.org) key.
   - `account_sid`: Your [Twilio](https://www.twilio.com) Account SID.
   - `auth_token`: Your [Twilio](https://www.twilio.com) Auth Token.
   - `from_="whatsapp:YOUR_TWILIO_NUMBER"`: Your Twilio WhatsApp-enabled number (e.g., `whatsapp:+1234567890`).
   - `to="whatsapp:DESTINATION_NUMBER"`: The recipient's WhatsApp number (e.g., `whatsapp:+0987654321`).

   Example:
   ```python
   STOCK_DATA_API_KEY = "your_alpha_vantage_api_key"
   NEWS_API_KEY = "your_newsapi_key"
   account_sid = "your_twilio_account_sid"
   auth_token = "your_twilio_auth_token"
   ```

## Usage
1. **Run the Script**:
   Execute the script using Python:
   ```bash
   python stock_notifier.py
   ```

2. **What to Expect**:
   - The script iterates through a predefined list of companies (e.g., Apple, Microsoft, etc.).
   - For each company, it:
     - Fetches daily stock data from [Alpha Vantage](https://www.alphavantage.co).
     - Calculates the percentage change between the previous day's closing price and the current day's opening price.
     - Retrieves the top three news articles from [NewsAPI](https://newsapi.org).
     - Sends a WhatsApp message via [Twilio](https://www.twilio.com) with the percentage change and news headlines.
   - If stock data is unavailable for a company, it prints an error message and skips to the next company.

3. **Sample Output** (WhatsApp Message):
   ```
   Apple Inc: 🔺 2.34%
   Headline: Apple unveils new iPhone model
   Brief: Apple announced the iPhone 15 with advanced features...
   Headline: Apple stock surges after earnings
   Brief: Strong quarterly earnings drive Apple's stock price...
   Headline: Apple partners with AI startup
   Brief: A new collaboration to enhance AI capabilities...
   ```

## Configuration
The script includes a list of companies to monitor, defined as a list of dictionaries:
```python
companies = [
    {"symbol": "AAPL", "name": "Apple Inc"},
    {"symbol": "MSFT", "name": "Microsoft Corp"},
    {"symbol": "GOOGL", "name": "Alphabet Inc"},
    # ... other companies
]
```
To monitor different companies, modify this list with the appropriate stock symbols and company names.

## Dependencies
- **requests**: For making HTTP requests to the [Alpha Vantage](https://www.alphavantage.co) API.
- **newsapi-python**: Python client for [NewsAPI](https://newsapi.org) to fetch news articles.
- **twilio**: Python client for [Twilio](https://www.twilio.com) to send WhatsApp messages.

## Error Handling
- If stock data is unavailable (e.g., due to API limits or invalid symbols), the script prints a message and continues with the next company.
- Ensure your API keys are valid and have sufficient quota to avoid rate-limiting issues.
- Twilio errors (e.g., invalid numbers) should be checked in the [Twilio](https://www.twilio.com) console.

## Limitations
- **API Rate Limits**:
  - [Alpha Vantage](https://www.alphavantage.co) free tier has a limit (e.g., 5 API calls per minute, 500 per day).
  - [NewsAPI](https://newsapi.org) free tier limits requests and article access.
  - [Twilio](https://www.twilio.com) has messaging limits based on your account plan.
- **Time Zone Considerations**: The script uses the most recent available dates from [Alpha Vantage](https://www.alphavantage.co), which may vary based on market hours and time zones.
- **WhatsApp Sandbox**: If using [Twilio](https://www.twilio.com)'s WhatsApp sandbox, users must opt-in by sending a message to the Twilio number first.

## Future Improvements
- Add support for scheduling the script to run daily using a cron job or similar.
- Include more detailed error logging to a file.
- Allow customization of the news query (e.g., date range, sources) using [NewsAPI](https://newsapi.org) advanced search options.
- Support additional notification channels (e.g., SMS, email) via [Twilio](https://www.twilio.com).
- Add a configuration file for easier management of API keys and company lists.

## Troubleshooting
- **API Key Errors**: Verify that your API keys for [Alpha Vantage](https://www.alphavantage.co), [NewsAPI](https://newsapi.org), and [Twilio](https://www.twilio.com) are correct and not expired.
- **Rate Limit Issues**: Check the API documentation for rate limits and upgrade to a paid plan if necessary.
- **Twilio Errors**: Ensure the `from_` and `to` numbers are WhatsApp-enabled and correctly formatted in the [Twilio](https://www.twilio.com) console.
- **No Stock Data**: Confirm that the stock symbol is valid and that the [Alpha Vantage](https://www.alphavantage.co) API is accessible.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, contact the project maintainer at [your-email@example.com].

## API References
- [Alpha Vantage](https://www.alphavantage.co): Provides real-time and historical stock market data.
- [NewsAPI](https://newsapi.org): Offers access to current and historic news articles from over 150,000 sources.
- [Twilio](https://www.twilio.com): Enables WhatsApp messaging and other communication channels.