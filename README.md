📈 Telegram Crypto Price Bot

Telegram Bot Username: @sohil_safari_crypto_bot

A simple Telegram bot that fetches real-time cryptocurrency prices from multiple Iranian exchanges and shows them in one response.

🚀 What This Bot Does

You send a crypto symbol (like btc, eth, etc.) to the bot, and it:

Fetches live prices from multiple exchanges

Collects the data concurrently using async requests

Returns formatted prices in Toman

Handles API errors gracefully

Example:

btc


Response:

قیمت لحظه‌ای BTC:

نوبیتکس: 3,245,000,000 تومان
رمزینکس: 3,240,500,000 تومان
بیت‌پین: 3,248,000,000 تومان
اکسیر: 3,242,000,000 تومان
والکس: 3,246,000,000 تومان

🏦 Supported Exchanges

Nobitex

Ramzinex

Bitpin

Exir

Wallex

Each exchange has its own symbol format, and the bot automatically converts the symbol correctly before sending the request.

🛠 Tech Stack

Python

pyTelegramBotAPI (telebot)

asyncio

httpx (async HTTP requests)

⚡ How It Works

Uses asyncio.gather() to fetch all prices simultaneously

Uses httpx.AsyncClient() for non-blocking API calls

Dynamically maps trading pair formats for each exchange

Uses infinity_polling() for continuous bot operation

The bot is designed to be lightweight and simple, while still demonstrating async programming and external API integration.

▶️ How to Run

Clone the repository:

git clone <your-repo-url>


Install dependencies:

pip install pyTelegramBotAPI httpx


Replace the bot token:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"


Run the script:

python bot.py

🔐 Important Note

Do not commit your real Telegram bot token.
Use environment variables instead:

import os
TOKEN = os.getenv("BOT_TOKEN")


Then create a .env file locally and add it to .gitignore.

💡 What I Practiced in This Project

Working with Telegram Bot API

Handling multiple async API calls

Formatting financial data

Basic error handling

Working with external REST APIs

📌 Future Improvements

Add inline keyboard buttons

Add caching system to reduce API calls

Deploy to a VPS or cloud service

Add logging system

Add price comparison / arbitrage detection
