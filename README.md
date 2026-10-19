# telestreamchat

**telestreamchat** is a local Telegram bot that reads all messages from a specific group and displays them in OBS Studio as a web page, so your viewers can see it on a screen.

## Quick start guide (Linux/macOS)

**Step 1:** create a virtual Python environment (optional) and install libraries

```
# Creating venv (skip for global requirements installation)
python -m venv venv
source venv/bin/activate

# Installing libraries
pip install -r requirements.txt
```

**Step 2:** creating a Telegram-bot profile. Use official [BotFather](https://t.me/BotFather) bot to create one.

**Step 3:** setting up environment. Copy a .env.example file as .env and open it in a text editor:

```
cp .env.example .env
nano .env # Nano is an example, you may use any text editor you like
```

Then paste a token you received from BotFather to `TELEGRAM_BOT_TOKEN`.

Other values from .env that usually don't require any changes:

`DATABASE_URL` is where your database is stored. Uses a local SQLite database by default, stored in data.db. You may also use any other database, but SQLite doesn't need any additional steps to set it up.

`SERVE_PORT` is where a local web application will accept connections.

**Step 4:** initializing database. telestreamchat uses databases with SQL support to store messages so they can be loaded even if program was restarted or crashed. Execute alembic migrations:

```
alembic upgrade head
```

Here, if you use SQLite database and it doesn't exist at a specified path, it will be created automatically.

**Step 5:** starting, adding to a group and getting chat ID.

telestreamchat will show messages from one specified chat only, other chats will be ignored. Status command will still work everywhere.

Start the bot:

```
python main.py
```

Add your bot to a desired Telegram chat, then type /status. If everything works, you will see such message in a chat which includes a chat ID. Copy this chat ID and paste it to a `TARGET_CHAT_ID` in .env, then stop a bot with Ctrl-C and start it again.

At this point, the bot is ready.

**Step 6: adding to OBS Studio**. In OBS Studio:

1. Click "Add source"
2. Select "Browser"
3. Type "http://localhost:1290" as a website path. If you changed `SERVE_PORT`, type an actual one instead of `1290`.
4. Done!

You may also try changing styles right in OBS Studio, for example fonts, colors, margins.
