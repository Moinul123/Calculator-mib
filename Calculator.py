import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('7150044305:AAHwaCBBP798BwlEMoyZiXHKc0r6SqZLgqU')

@bot.message_handler(func=lambda message: True)
def calculate(message):
    try:
        result = eval(message.text)
        bot.reply_to(message, f"{message.text} = {result}")
    except:
        bot.reply_to(message, "Sorry, I couldn't understand the calculation.")

bot.polling()
