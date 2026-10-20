import funcs
funcs.load_env()

import os
import sys
import telebot
import log
import models
import db
import memory
from sqlalchemy import select
import web
import threading

required_vars = ['DATABASE_URL', 'TELEGRAM_BOT_TOKEN', 'SERVE_PORT']
vars_ready = True
for rvar in required_vars:
    if not rvar in os.environ:
        print(f'You forgot to set {rvar} environment variable. Please check your .env', file=sys.stderr)
        vars_ready = False

if not vars_ready:
    print('The script is not ready to start.', file=sys.stderr)

with db.Session() as session:
    stmt = select(models.Message)
    for message in session.scalars(stmt).all():
        memory.loaded_messages.append(funcs.db_message_to_dict(message))

# Since this moment, the script is finally ready to start.

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

@bot.message_handler(commands=['status'])
def on_command_start(msg):
    log.message_log(msg)
    bot.send_message(msg.chat.id, f"Working. Chat id = {msg.chat.id}")

@bot.message_handler()
def on_message(msg):
    log.message_log(msg)
    if msg.chat.type not in ['supergroup', 'group']:
        return
    if not 'TARGET_CHAT_ID' in os.environ:
        log.userwarn("A TARGET_CHAT_ID environment variable is not set, so the last message is ignored. Make sure you restarted the bot after setting TARGET_CHAT_ID.")
        return
    if msg.chat.id != int(os.environ['TARGET_CHAT_ID']):
        return

    with db.Session() as session:
        new_message = models.Message(
            author_tgid=msg.from_user.id,
            author_username=msg.from_user.username,
            content=msg.text)
        session.add(new_message)
        session.commit()
        session.flush()
        memory.loaded_messages.append(funcs.db_message_to_dict(new_message))

# Start a web thread
web_thread = threading.Thread(target=lambda: web.app.run(port=os.environ['SERVE_PORT']))
web_thread.start()

bot.polling(non_stop=True)

