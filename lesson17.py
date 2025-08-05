# 27 dars kiril lotin telegram bot
from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = "8328567715:AAHpYTrc0dLXj5E3i5i_KJWGyJOvfy-iK1Y"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu aleykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()
# matn = input("Matn kiritng: ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))