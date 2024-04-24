import asyncio
import time
from telegram import Bot
from apiRequest.api_request import generate_recipe
from dotenv import dotenv_values
from database.firebaseFuncs import *
import schedule

config = dotenv_values(".env")
bot = Bot(token=config["bot_token"])
chat_id = config["chat_id"]

async def send_daily_message():
    today_plate= getTodaysMeal()
    recipe =  generate_recipe(today_plate)
    message = f"El plato de hoy es: {today_plate}:\n\nUna idea para prepararlo es:\n{recipe}"
    await bot.send_message(chat_id=chat_id, text=message)

def schedule_daily_message():
    schedule.every().day.at('18:19:00').do(asyncio.run, send_daily_message())

def run_schedule():
    schedule_daily_message()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_schedule()
