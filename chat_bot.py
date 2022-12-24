
import telebot
import random
#import model
from cfg import TOKEN
from random import randint



candy = dict()

def end_game(message):
	bot.send_message(message.chat.id, 'Конец игры')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message, res=False):
	bot.send_message(message.chat.id, 'Игра "117 конфет, за 1 ход можно брать не более 28 конфет"')
	bot.send_message(message.chat.id, 'Введите количество конфет')
	candy[message.chat.id] = 117

@bot.message_handler(content_types=["text"])

def handle_text(message):
	
	if int(message.text) > 28 or int(message.text) < 1:
		bot.send_message(message.chat.id, 'Не корректный ввод')
		bot.send_message(message.chat.id, 'Переход хода к боту')
		
	else:
		candy[message.chat.id] = candy[message.chat.id] - int(message.text)
		bot.send_message(message.chat.id, f'Осталось {str(candy[message.chat.id])} конфет')
	if candy[message.chat.id] <= 28 and candy[message.chat.id] > 0:
		bot.send_message(message.chat.id, 'Победил бот')
		end_game(message)
	elif candy[message.chat.id] == 0:
		bot.send_message(message.chat.id, 'Победил пользователь')
		end_game(message)
	else:
		rand = random.randint(1, 28)
		candy[message.chat.id] = candy[message.chat.id] - rand
	bot.send_message(message.chat.id, f'Бот забрал {rand} конфет, осталось {str(candy[message.chat.id])} конфет')
	bot.send_message(message.chat.id, 'Введите количество конфет')
	
bot.infinity_polling()
