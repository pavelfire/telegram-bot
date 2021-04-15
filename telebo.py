#https://tproger.ru/translations/telegram-bot-create-and-deploy/
import telebot
bot = telebot.TeleBot('TOKEN')

#обработка команд старт и хелп
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

#обработка сообщений ответ бота
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == '':
        bot.send_message(message.from_user.id, 'Скажи что нибудь.')
    elif message.text.lower() == 'Как дела?':
        bot.send_message(message.from_user.id, 'У меня всё хорошо. А как у тебя?')
    elif message.text.lower() == 'Как тебя зовут?':
        bot.send_message(message.from_user.id, 'Меня зовут помошник.')
    elif message.text.lower() == 'погода':
        bot.send_message(message.from_user.id, 'Сейчас на улице хорошая погода.')
    elif message.text.lower() == 'анекдот':
        bot.send_message(message.from_user.id, 'На завтра ничего не планируйте — будет банкет. — Так банкет же сегодня? — Вот я и говорю, на завтра ничего не планируйте. anekdotov.net')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

bot.polling(none_stop=True)


#pip install virtualenv
#virtualenv my_env
#cd my_env
#U:\Git\bin\git clone https://github.com/pavelfire/telegram-bot.git
#scripts\activate.bat
#cd telegram-bot
#pip install requests
#создаём список зависимостей
#pip freeze > requirements.txt
#add file Procfile.windows with content web: python telebo.py
#add file __init__.py it can be empty
#U:\Git\bin\git init
#U:\Git\bin\git add .
#U:\Git\bin\git commit -m "first commit - comment"
#U:\Git\bin\git push -u  https://github.com/pavelfire/telegram-bot.git

