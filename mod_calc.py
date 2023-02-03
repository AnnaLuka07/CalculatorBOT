from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, messagehandler, filters, InlineQueryHandler, CommandHandler,ConversationHandler
from logg import logger

#Функции калькулятора
def sum(update, _):
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')

def sub(update, _):
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} - {y} = {x - y}')

def mult(update, _):
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')

def dev(update, _):
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} * {y} = {x * y}')
    if y != 0:
        update.message.reply_text(f'{x} * {y} = {x * y}')
    else:
        print('На 0 делить нельзя!')

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(' Будет скучно - пиши.', reply_markup=ReplyKeyboardRemove())
    # Заканчиваем разговор.
    return ConversationHandler.END

