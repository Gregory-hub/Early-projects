import telebot as t

bot = t.TeleBot(token="987034020:AAG57WOK0qY-P4BQkx9l2c1iFbY_MDzonws")
print("The bot is running")

@bot.message_handler(content_types=['text'])
def echo(message):
	send_data = message.text
	m = message.text.split()
	print(m)
	try:
		if m[0] == '#sum':
			send_data = sum(map(float, m[1:]))
			if str(send_data).endswith('.0'):
				send_data = int(send_data)
	except:
		send_data = 'Error'
	bot.send_message(message.from_user.id, send_data)


bot.polling()