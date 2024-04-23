import asyncio
from telegram import Bot
import schedule
import time
from apiRequest.api_request import generate_recipe
from dotenv import dotenv_values
config = dotenv_values(".env")
bot = Bot(token=config.bot_token)
chat_id = config.chat_id
plate = 'Pollo a la parmesana'

async def send_daily_message():
    
    recipe = generate_recipe(plate)
    print(recipe)
    message=plate + ":\nUna idea para preparar es:" + recipe
    await bot.send_message(chat_id=chat_id, text=message)



schedule.every().day.at('00:17:05').do(asyncio.run, send_daily_message())

while True:
    schedule.run_pending()
    time.sleep(1)
