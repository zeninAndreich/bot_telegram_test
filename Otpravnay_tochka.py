import telebot
from config import token

#telebot.apihelper.ENABLE_MIDDLEWARE = True (обработчик промежуточного слоя)
myBot = telebot.TeleBot(token)
name = ''

@myBot.message_handler(commands = ['start'])
def start_message(message):
    myBot.send_message(message.chat.id,'Привет, мой догорой друг!!!')
    mark_up = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton('Помогите!!! ')
    btn2 = telebot.types.KeyboardButton('Все пока!!! ')
    btn3 = telebot.types.KeyboardButton('Кнопка на запас!!! ')
    mark_up.row(btn1,btn2)
    mark_up.row(btn3)
    myBot.send_message(message.chat.id, 'Мы тут сделали управление:',reply_markup=mark_up)
    with open('logi_start.txt','a') as f:
        print(message.from_user.username,file=f)


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
    my_keyboard = telebot.types.InlineKeyboardMarkup()
    key_one = telebot.types.InlineKeyboardButton(text = 'Больше 18', callback_data=1)
    key_two = telebot.types.InlineKeyboardButton(text = 'Меньше 18', callback_data=2)
    my_keyboard.add(key_one)
    my_keyboard.add(key_two)
    myBot.send_message(message.chat.id, 'Сколько тебе лет? ',reply_markup=my_keyboard)


@myBot.callback_query_handler(func = lambda call: True)
def callback_keyboard(call):
    if call.data == '1':
        myBot.send_message(call.message.chat.id, 'Тебе уже можно все!!! ')
    if call.data == '2':
        myBot.send_message(call.message.chat.id, 'Пока ничего нельзя!!!')


#@myBot.message_handler(content_types= ['voice'])
#def voice_message(message):
    #myBot.send_message(message.chat.id, ' Ой,как же я не люблю эти голосовые сообщения!!!')

#@myBot.middleware_handler(update_types=['message'])
#def mess_up(bot_instance, message):
    #myBot.send_message(message.chat.id, message.text+'!!!!! ахахах')

myBot.infinity_polling()