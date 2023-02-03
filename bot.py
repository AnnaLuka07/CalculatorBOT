from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler, CommandHandler, ConversationHandler
from config import TOKEN
import logg
from mod_calc import *

# Создаем Updater и передаем ему токен бота.
updater = Updater(token=TOKEN, use_context=True)

# получаем диспетчера для регистрации обработчиков
dispatcher = updater.dispatcher

# Определяем константы этапов разговора
CALC, INPUT, SUM, SUB, MULTH, DIV = range(6)


# функция обработки команды /start
def start(update, context):
    reply_keyboard = [['Начать!']]  # Создадим кнопку для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)  # Создаем простую клавиатуру для ответа
    # Начинаем разговор.
    context.bot.send_message(chat_id=update.effective_chat.id, text=
    f'Привет {update.effective_user.first_name}! Добро пожаловать в калькулятор. Чтобы приступить нажми "Начать!".',
              reply_markup=markup_key, )
    return CALC

def calk(update, context):
    if update.message.reply_text == ['Начать!']:
        markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        reply_keyboard = [['Сумма', 'Разность', 'Умножение', 'Деление']]  
        context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите операцию, которую ты хочешь выполнить",reply_markup=markup_key,)
        return INPUT
   

# def input_num(update, _):
#    msg  = update.message.reply_text("Введите 2 числа через пробел")
#    items = msg.split(' ')
#    x = int(items[1])
#    y = int(items[2])
#    return items    


# Conv_halder = CommandHandler('start', start)

com_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        CALC: [MessageHandler(Filters.regex('^(Сумма|Разность|Умножение|Деление)$'), calk)],
        # INPUT: [messagehandler(filters.regex('^()$'), op)]},
    }, fallbacks=[CommandHandler('cancel', cancel)], )  # точка выхода из разговора

# Обработчик разговоров
dispatcher.add_handler(com_handler)

# старт бота
updater.start_polling()
updater.idle()
