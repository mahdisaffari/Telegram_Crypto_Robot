"This is user_name of bot in telegram :@sohil_safari_crypto_bot"
import telebot
import asyncio
import httpx

TOKEN = "Your token bot."
bot = telebot.TeleBot(TOKEN)

def get_symbol_for_exchange(symbol, exchange):
    s = symbol.lower()
    if exchange == "nobitex":
        return f"{s}irt"
    elif exchange == "raminex":
        return f"{s}/IRT"
    elif exchange == "bitpin":
        return f"{s}_irt"
    elif exchange == "exir":
        return f"{s}-irt"
    elif exchange == "wallex":
        return f"{s.upper()}IRT"
    else:
        return s

async def fetch_nobitex(symbol):
    try:
        s = get_symbol_for_exchange(symbol, "nobitex")
        async with httpx.AsyncClient() as client:
            res = await client.get(f'https://api.nobitex.ir/v2/orderbook/{s}')
            price = res.json()['asks'][0][0]
            return f" نوبیتکس: {price} تومان"
    except:
        return " نوبیتکس: خطا"

async def fetch_raminex(symbol):
    try:
        target_symbol = get_symbol_for_exchange(symbol, "raminex")
        async with httpx.AsyncClient() as client:
            res = await client.get("https://api.ramzinex.com/public/v1/market/stats")
            data = res.json()["data"]
            for item in data:
                if item['fa'] == target_symbol:
                    return f" رمزینکس: {item['latest']:,} تومان"
            return " رمزینکس: پیدا نشد"
    except:
        return " رمزینکس: خطا"

async def fetch_bitpin(symbol):
    try:
        target_symbol = get_symbol_for_exchange(symbol, "bitpin")
        async with httpx.AsyncClient() as client:
            res = await client.get("https://api.bitpin.ir/v1/mkt/markets/")
            data = res.json()['results']
            for k, v in data.items():
                if v['code'] == target_symbol:
                    return f" بیت‌پین: {int(v['price']):,} تومان"
            return " بیت‌پین: پیدا نشد"
    except:
        return " بیت‌پین: خطا"

async def fetch_exir(symbol):
    try:
        target_symbol = get_symbol_for_exchange(symbol, "exir")
        async with httpx.AsyncClient() as client:
            res = await client.get(f"https://api.exir.io/v1/ticker?symbol={target_symbol}")
            price = res.json()['last']
            return f" اکسیر: {int(price):,} تومان"
    except:
        return " اکسیر: خطا"

async def fetch_wallex(symbol):
    try:
        target_symbol = get_symbol_for_exchange(symbol, "wallex")
        async with httpx.AsyncClient() as client:
            res = await client.get("https://api.wallex.ir/v1/markets")
            data = res.json()['result']
            for m in data:
                if m['symbol'] == target_symbol:
                    return f" والکس: {int(m['stats']['latest']):,} تومان"
            return " والکس: پیدا نشد"
    except:
        return " والکس: خطا"

async def get_all_prices(symbol):
    tasks = [
        fetch_nobitex(symbol),
        fetch_raminex(symbol),
        fetch_bitpin(symbol),
        fetch_exir(symbol),
        fetch_wallex(symbol),
    ]
    results = await asyncio.gather(*tasks)
    return "\n".join(results)

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    symbol = message.text.lower()
    try:
        result = asyncio.run(get_all_prices(symbol))
        bot.reply_to(message, f" قیمت لحظه‌ای {symbol.upper()}:\n\n{result}")
    except Exception as e:
        bot.reply_to(message, f"خطا در پردازش درخواست: {e}")

print(" ربات اجرا شد...")
bot.infinity_polling()
