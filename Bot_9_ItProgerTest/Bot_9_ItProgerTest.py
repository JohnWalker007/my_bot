import telebot
import webbrowser
from telebot import types as tp
bot = telebot.TeleBot('7055181662:AAF4ZbWfVV6bX9KfFqGOaZkYAmj1liCRV5g')

#python Bot_9_ItProgerTest.py



@bot.message_handler(commands=['start'])
def start(message):
	markup = tp.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = tp.KeyboardButton('Перейди на сайт')
	markup.add(item1)
	item2 = tp.KeyboardButton('Удалить фото')
	item3 = tp.KeyboardButton('Редактировать текст')
	markup.add(item2, item3)

	file = open('Castle.jpg', 'rb')
	bot.send_photo(message.chat.id, file, reply_markup=markup)
	#bot.send_message(message.chat.id, 'Привет ' + str(message.from_user.first_name), reply_markup=markup)
	bot.register_next_step_handler(message, on_click)

def on_click(message):
	if message.text == 'Перейди на сайт':
		bot.send_message(message.chat.id, 'Hahahah-ha-ha!')
	elif message.text == 'Удалить фото':
		bot.send_message(message.chat.id, 'Delete it')




@bot.message_handler(commands=['site', 'website'])
def site(message):
	webbrowser.open('https://porsche.ru/models/911/index.html?ysclid=ltn4we2n1f427552846')



@bot.message_handler(content_types=['photo'])
def get_photo(message):
	markup = tp.InlineKeyboardMarkup()
	item1 = tp.InlineKeyboardButton('Перейди на сайт', url='https://google.com')
	markup.row(item1)
	item2 = tp.InlineKeyboardButton('Удалить фото', callback_data='delete')
	item3 = tp.InlineKeyboardButton('Редактировать текст', callback_data='edit')
	markup.row(item2, item3)

	bot.reply_to(message, 'Вау, как красиво!', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
	if callback.data == 'delete':
		bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
	elif callback.data == 'edit':
		bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



@bot.message_handler(commands=['photo'])
def send_photo(message):
	photo = open('Castle.jpg', 'rb')
	bot.send_photo(message.chat.id, photo)

#python Bot_9_ItProgerTest.py

@bot.message_handler(commands=['main', 'hello'])
def start(message):
	bot.send_message(message.chat.id, f'Привет! <u><i>{message.from_user.first_name}</i> {message.from_user.last_name}</u>', parse_mode='html')



@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '<b>Help me!</b>', parse_mode='html')



@bot.message_handler(content_types=['text'])
def hi(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, f'Привет! <u><i>{message.from_user.first_name}</i> {message.from_user.last_name}</u>', parse_mode='html')
	elif message.text.lower() == 'id':
		bot.reply_to(message, f'ID: {message.from_user.id}')



bot.polling(non_stop=True)
#python Bot_9_ItProgerTest.py