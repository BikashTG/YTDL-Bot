import telebot
import re
import os
from Extra.classes import replies
from Extra.functions import is_supported, download
from Extra.messages import print_log, print_log_simple, print_except

token = os.environ['TELEGRAM_TOKEN'] #GET TOKEN FROM HEROKU
bot = telebot.TeleBot(token) # OG BOT
#bot = telebot.TeleBot("***REMOVED***") #TEST BOT

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == 'help':
        bot.edit_message_text(replies.WELCOME + '\n' + '\n' + 'HELP ⬇️', chat_id=msgcid, message_id= msgid)
        help_message(call.message)
    if call.data == 'errors':
        bot.edit_message_text(replies.WELCOME + '\n' + '\n' + 'ERRORS INFO ⬇️', chat_id=msgcid, message_id= msgid)
        errors_info(call.message)
    if call.data == 'dl':
        bot.answer_callback_query(call.id, text='MP4 Download Selected')
        bot.edit_message_text(text= '<b>URL: </b>' + '' + url + '<b>\nSelect Download Option:</b> MP4', chat_id= msgcid, message_id= msgid, disable_web_page_preview=True, parse_mode='HTML')
        dl(call.message)
    if call.data == 'dlmp3':
        bot.answer_callback_query(call.id, text='MP3 Download Selected')
        bot.edit_message_text(text= '<b>URL: </b>' + '' + url + '<b>\nSelected Download Option:</b> MP3', chat_id= msgcid, message_id= msgid, disable_web_page_preview=True, parse_mode='HTML')
        dlmp3(call.message)
    if call.data == 'howto':
        bot.edit_message_text(replies.WELCOME + '\n' + '\n' + 'HOW TO DOWNLOAD ⬇️', chat_id=msgcid, message_id= msgid)
        how_to_message(call.message)

@bot.message_handler(commands=['dl', 'dlmp3']) #CHECK FOR /errors
def new_way(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='ℹ️ How to download ℹ️', callback_data='howto'))
    bot.reply_to(message, replies.NEW_WAY, reply_markup=markup)

@bot.message_handler(commands=['start']) #CHECK FOR /start
def start_message(message):
    global url
    global msgid
    global msgcid
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='ℹ️ How to download ℹ️', callback_data='howto'))
    markup.add(telebot.types.InlineKeyboardButton(text='ℹ️ Help ℹ️', callback_data='help'))
    markup.add(telebot.types.InlineKeyboardButton(text='🚨 Errors Info 🚨', callback_data='errors'))
    print_log_simple('start', message.chat.id)
    msg = bot.send_message(message.chat.id, replies.WELCOME, reply_markup=markup)
    msgid = msg.message_id
    msgcid = msg.chat.id

@bot.message_handler(commands=['help']) #CHECK FOR /help
def help_message(message):
    print_log_simple('help', message.chat.id)
    bot.send_message(message.chat.id, replies.HELP)

@bot.message_handler(commands=['howto'])
def how_to_message(message):
    bot.send_message(message.chat.id, replies.HOW_TO)

@bot.message_handler(commands=['errors']) #CHECK FOR /errors
def errors_info(message):
    print_log_simple('errors', message.chat.id)
    bot.send_message(message.chat.id, replies.ERRORS)

@bot.message_handler(regexp=(r'(https?://\S+)'))
def function_name(message):
    try:
        global url
        global msgid
        global msgcid
        url = re.search("(?P<url>https?://[^\s'\"]+)", message.text).group("url")
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='MP4 📹', callback_data='dl'))
        markup.add(telebot.types.InlineKeyboardButton(text='MP3 🎵', callback_data='dlmp3'))
        msg = bot.send_message(message.chat.id, '<b>URL: </b>' + '' + url + '<b>\nSelect Download Option</b> ⬇️', reply_markup=markup, disable_web_page_preview=True, parse_mode='HTML')
        msgid = msg.message_id
        msgcid = msg.chat.id
    except Exception as exception:
        print_except(exception, message.chat.id, url, bot)

@bot.message_handler(regexp="")
def no_url(message):
    print_log('URL', 'URL_ERROR', message.chat.id, 'NO_URL', message, bot)

def dl(message):
    try:
        url = message.text.split()[1]
        if is_supported(url, message.chat.id, bot): #CHECK IF URL IS SUPPORTED
            lurl = re.findall(r'(https?://\S+)', url)
            download('video', 'OK', message.chat.id, url, message, bot, lurl)
        else:
            print_log('video', 'SUPP_ERROR', message.chat.id, url, message, bot)
    except Exception as exception:
        print_except(exception, message.chat.id, url, bot)

def dlmp3(message):
    try:
        url = message.text.split()[1]
        if is_supported(url, message.chat.id, bot): #CHECK IF URL IS SUPPORTED
            lurl = re.findall(r'(https?://\S+)', url)
            download('audio', 'OK', message.chat.id, url, message, bot, lurl)
        else:
            print_log('audio', 'SUPP_ERROR', message.chat.id, url, message, bot)
    except Exception as exception:
        print_except(exception, message.chat.id, url, bot)

bot.polling()
