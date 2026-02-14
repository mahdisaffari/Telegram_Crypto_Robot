"This is user_name of bot in telegram :@sohiel_price_dollar_bot"

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
token = "Your telegram token."

def get_dollar_price():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.tgju.org/profile/price_dollar_rl"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.find("span", {"data-col": "info.last_trade.PDrCotVal"})

    if price_tag:
        return f"قیمت دلار امروز: {price_tag.text.strip()} تومان"
    else:
        return "❌ نتوانستم قیمت دلار را از سایت دریافت کنم."


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! برای دریافت قیمت دلار بنویس /price")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price_text = get_dollar_price()
    await update.message.reply_text(price_text)

if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    app.run_polling()
   