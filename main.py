import logging
import os
from dotenv import load_dotenv
from telegram import Update
from jokes import getJoke
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters


load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # if(update)
    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=getJoke().setup + " \n " + getJoke().punchline)
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry no more jokes for the day")

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('BOT_TOKEN')).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
    
    application.run_polling()