import asyncio
import threading
import time
from telegram import Bot, Update
from telegram.ext import *
from apiRequest.api_request import generate_recipe
from dotenv import dotenv_values
from database.firebaseFuncs import *
import handleCommands.commandHandler as commandHandler
import schedule

config = dotenv_values(".env")



async def send_daily_message():
    try:
        bot = Bot(token=config["bot_token"])
        chat_id = config["chat_id"]
        today_plate = getTodaysMeal()
        recipe = generate_recipe(today_plate)
        message = f"El plato de hoy es: {today_plate}:\n\nUna idea para prepararlo es:\n{recipe}"
        await bot.send_message(chat_id=chat_id, text=message)
    except:
        print("Error sending message")

def schedule_daily_message():
    schedule.every().day.at('19:28:40').do(run_async_in_thread, send_daily_message)

def run_async_in_thread(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro())

def run_schedule():
    schedule_daily_message()
    while True:
        schedule.run_pending()
        time.sleep(1)

async def start_commmand(update, context):
    await update.message.reply_text('Hello! Welcome To Store!')

def main():
    application = Application.builder().token(config["bot_token"]).build()
    application.add_handler(CommandHandler('setMenu', commandHandler.update_meal_handler))
    application.run_polling(1.0)
    

if __name__ == "__main__":
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()

    main()
