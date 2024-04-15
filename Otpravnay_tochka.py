import telebot
from config import token

#telebot.apihelper.ENABLE_MIDDLEWARE = True (обработчик промежуточного слоя)
myBot = telebot.TeleBot(token)
name = ''

@myBot.message_handler(commands = ['start'])
def start_message(message):
    myBot.send_message(message.chat.id,'Привет, мой догорой друг!!!')

@myBot.message_handler(commands=['help'])
def help_message(message):
    myBot.send_message(message.chat.id,'Раздел помощи находится в разработке :(')
    print(message.from_user.id)

@myBot.message_handler(content_types=['text'])
def hello_message(message):
    if message.text.lower() == 'привет':
        myBot.send_message(message.chat.id, 'И тебе привет!!!)',reply_to_message_id=message.id)
        myBot.send_message(message.chat.id, 'Как тебя зовут?)')
        myBot.register_next_step_handler(message,reg_name)
def reg_name(message):
    global name
    name = message.text
    myBot.send_message(message.chat.id, f'Рад приветствовать тебя {name} !!! :)')

#@myBot.message_handler(content_types= ['voice'])
#def voice_message(message):
    #myBot.send_message(message.chat.id, ' Ой,как же я не люблю эти голосовые сообщения!!!')

#@myBot.middleware_handler(update_types=['message'])
#def mess_up(bot_instance, message):
    #myBot.send_message(message.chat.id, message.text+'!!!!! ахахах')

myBot.infinity_polling()