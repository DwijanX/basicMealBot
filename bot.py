import asyncio
import time
from telegram import Bot
from apiRequest.api_request import generate_recipe
from dotenv import dotenv_values
import schedule

config = dotenv_values(".env")
bot = Bot(token=config["bot_token"])
chat_id = config["chat_id"]
plate = 'Pollo a la parmesana'

async def send_daily_message():
    recipe =  generate_recipe(plate)
    message = f"{plate}:\nUna idea para preparar es:\n{recipe}"
    await bot.send_message(chat_id=chat_id, text=message)

def schedule_daily_message():
    schedule.every().day.at('00:28:45').do(asyncio.run, send_daily_message())

def run_schedule():
    schedule_daily_message()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
