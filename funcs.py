# funcs.py
# This script defines functions that will be used in several places, not just once in a script

import os

def load_env():
    if os.path.exists('.env'):
        with open('.env', 'r', encoding='utf-8') as f:
            content = f.read()
        for line in content.split('\n'):
            if len(line) == 0 or line[1] == '#':
                continue
            key, value = line.split('=')
            if not key in os.environ:
                os.environ[key] = value

def db_message_to_dict(message):
    return {
        'id': message.id,
        'author_username': message.author_username,
        'content': message.content
    }
