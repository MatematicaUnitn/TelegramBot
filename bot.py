import telebot

# Setup del bot
bot = telebot.TeleBot('2095077251:AAHSBgqqsjG23YigKDT43o-18BhDjiEj1SM')

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['start'])
def prova(message):
  bot.send_message(message.chat.id, "Hello! \n sus")
  bot.send_message(message.chat.id, "bye")

bot.polling()
