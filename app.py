import telebot

bot = telebot.TeleBot("993140269:AAFrjY6nrbFGKpaW0aW_nDoSLvb27Q5Ei7k")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop=True )