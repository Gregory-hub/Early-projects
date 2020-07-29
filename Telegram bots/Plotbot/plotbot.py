from telebot import *
import matplotlib.pyplot as plt

bot = TeleBot(token = "959687516:AAGvzEN-ng0hs5Jpbw4W52kD8BaMAJwJDH4")


@bot.message_handler(commands=['plot'])
def send_plot(message):
	print("Fun 'send_plot' is called")
	bot.send_message(message.from_user.id, "Enter function of plot as a mathematitian-pythoner(like y = x**2 or y = 1/(x-3)")

	@bot.message_handler(content_types=['text'])
	def plot(message):
		try:
			fun = message.text		
			fun = fun.replace("y = ", "")
			fun = fun.replace("y=", "")
			print("fun:", fun)

										# Now we have xs and ys

			plt.style.use('fivethirtyeight')

			
			
			plt.savefig('plot.png')
			bot.send_photo(message.from_user.id, open("plot.png", 'rb'))
		except:
			bot.send_message(message.from_user.id, "Not OK")


@bot.message_handler(commands=['start'])
def st(message):
	bot.send_message(message.from_user.id, "You sent me the command 'start'")

print("Bot has started")
bot.polling()