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
import os
from flask import Flask

config = dotenv_values(".env")

print("running chat", config["chat_id"])

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
        await bot.send_message(chat_id=chat_id, text="No pude enviar el plato de hoy, si no registraste un menu este mes prueba usar el comando /generateMenu o agregalo tu con /setMenu")

def schedule_daily_message():
    schedule.every().day.at('09:00:00',"America/La_Paz").do(run_async_in_thread, send_daily_message)

def run_async_in_thread(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coro())

def run_schedule():
    schedule_daily_message()
    while True:
        schedule.run_pending()
        time.sleep(1)



def main():
    application = Application.builder().token(config["bot_token"]).build()
    application.add_handler(CommandHandler('setMenu', commandHandler.update_meal_handler))
    application.add_handler(CommandHandler('generateMenu', commandHandler.generate_meals))
    application.add_handler(CommandHandler('getToday', commandHandler.get_today_meal))
    application.run_polling(1.0)
    
app = Flask(__name__)

@app.route('/')
def health_check():
    return 'OK'

def run_flask_app():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.start()

    main()
