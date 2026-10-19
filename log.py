import datetime

def _timestamp():
    return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

def message_log(msg):
    print(f'[ MESSAGE {_timestamp()} {msg.from_user.username} ] {msg.text}')

def userwarn(text):
    print(f'[ USERWARN {_timestamp()} ] {text}')

