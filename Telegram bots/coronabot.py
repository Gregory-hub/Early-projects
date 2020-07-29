from bs4 import BeautifulSoup
import requests as rq
import telebot as tb


def get_corona_dict():
	print('get_corona_dict was called')
	html = rq.get('https://index.minfin.com.ua/reference/coronavirus/geography/').text
	soup = BeautifulSoup(html, 'lxml')

	soup = soup.find('table', class_='line')

	content = []
	for tr in soup.findAll('tr'):
		local = []
		for td in tr.findAll('td'):
			local.append(td.text.replace('\\xad', '-')) if td.text != '' else local.append('0')
		if local == []: continue
		local.pop(7)
		local.pop(4)
		local.pop(2)
		content.append(local)

	tab_names = ['infection', 'deaths', 'well_being', 'sick']

	corona_dict = {}

	for i in range(len(content)):
		values = {}
		for key, val in zip(tab_names, content[i][1:]):
			values[key] = val
		corona_dict[content[i][0]] = values
	return corona_dict

# corona_dict is available({country:{'infection':infection, 'deaths':deaths, 'well-being':well-being, 'sick':sick}})

bot = tb.TeleBot('1106645639:AAFFE5SEbyoZ-UsDtz_h8O18El3F_UwCAIw')


@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.from_user.id, "Комманды:\n'/infection <Страна>' - Всего зара­жений\n'/deaths <Страна>' - Смер­тельные случаи\n'/well_being <Страна>' - Выздоро­вевшие\n'/sick <Страна>' - Сейчас болеют\n'/AllInfo <Страна>' - Вся информация")


@bot.message_handler(commands=['infection'])
def infection(message):
	country = message.text[message.text.index('infection')+len('infection'):].strip()
	print(country)
	try:
		corona_dict = get_corona_dict()
		country_info = corona_dict[country.capitalize() if country != "США" else country]
		ancwer = country.capitalize() + ' - количество заражённых: ' + country_info['infection']
		bot.send_message(message.from_user.id, ancwer)
	except:
		bot.send_message(message.from_user.id, "Error")


@bot.message_handler(commands=['deaths'])
def deaths(message):
	country = message.text[message.text.index('deaths')+len('deaths'):].strip()
	print(country)
	try:
		corona_dict = get_corona_dict()
		country_info = corona_dict[country.capitalize() if country != "США" else country]
		ancwer = country.capitalize() + ' - количество смертей: ' + country_info['deaths']
		bot.send_message(message.from_user.id, ancwer)
	except:
		bot.send_message(message.from_user.id, "Error")


@bot.message_handler(commands=['well_being'])
def well_being(message):
	country = message.text[message.text.index('well_being')+len('well_being'):].strip()
	print(country)
	try:
		corona_dict = get_corona_dict()
		country_info = corona_dict[country.capitalize() if country != "США" else country]
		ancwer = country.capitalize() + ' - количество выздоро­вевших: ' + country_info['well_being']
		bot.send_message(message.from_user.id, ancwer)
	except:
		bot.send_message(message.from_user.id, "Error")


@bot.message_handler(commands=['sick'])
def sick(message):
	country = message.text[message.text.index('sick')+len('sick'):].strip()
	print(country)
	try:
		corona_dict = get_corona_dict()
		country_info = corona_dict[country.capitalize() if country != "США" else country]
		ancwer = country.capitalize() + ' - количество больных: ' + country_info['sick']
		bot.send_message(message.from_user.id, ancwer)
	except:
		bot.send_message(message.from_user.id, "Error")


@bot.message_handler(commands=['AllInfo'])
def All_Info(message):
	country = message.text[message.text.index('AllInfo')+len('AllInfo'):].strip()
	print(country)
	try:
		corona_dict = get_corona_dict()
		country_info = corona_dict[country.capitalize() if country != "США" else country]
		ancwer = 'Заражённых: ' + country_info['infection'] + '\nСмертей: ' + country_info['deaths'] + '\nВыздоровевших: ' + country_info['well_being'] + '\nБольных: ' + country_info['sick']
		bot.send_message(message.from_user.id, ancwer)
	except:
		bot.send_message(message.from_user.id, "Error")


print('Bot is working')
bot.polling()