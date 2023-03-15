# ⚠️ This version of the bot is no longer updated!
Now I'm rewriting the bot, follow the updates on the rewrite branch :)
<br>

## 🪲 In case of errors, open a ticket in the Issues tab :)

# Navigation

- [Navigation](#navigation)
- [Why do we need this bot?](#why-do we-need-this-bot)
- [Installation](#installation)
      -[Python](#python)
      - [Install required Python packages](#install required python packages)
      - [Run installer](#run-installer)
      - [Launch bot](#start-bot)
           - [Run with script](#run-with-script)
                - [Linux](#linux)
                - [Macos](#macos)
           - [Start manually](#start-manually)
- [Debug mode](#debug-mode)

# Why is this bot needed?

Often, people who want to start a small online business do so through a social media profile, which requires them to manually process each application. This bot will allow everyone to quickly open an automated store based on a telegram bot, which will significantly reduce the order processing time.

![overview](DOCS/bot_overview.gif)

# Installation

##Python

For the bot to work, [Python version 3.10 and higher](https://www.python.org/downloads/) must be installed.

## Install required Python packages

     python3 -m pip install -r requirements.txt

## Run the installer

Before launching the installer, you need to [create a token](https://youtu.be/fyISLEvzIec) for the telegram bot and [get your ID](https://badcode.ru/kak-v-telegram-uznat-svoi-id/) .

The installer is launched with the command:

     python3 installer.py

## Run the bot

### Launch via script

#### Linux/MacOS

     $ chmod +x start.sh
     $ ./start.sh

#### Windows

     $start.cmd

### Start manually

     python3 main.py

# Debug mode

Debug mode can be activated in the "General Settings" tab.
After activation, the terminal will display all messages and calls in the format:

     DEBUG: <MESSAGE/CALL> [<user_id>] <Message/Call>

*Example: `DEBUG CALL [462741] admin_itemManagement`*