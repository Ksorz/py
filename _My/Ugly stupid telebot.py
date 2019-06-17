import telebot

bot = telebot.TeleBot("770544842:AAETUFb9uMC9TYOioSyR7SVodxDou-leOZ0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	# bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
