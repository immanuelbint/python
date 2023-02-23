#!/usr/bin/env python
# Testing telegram bot

import os
import telebot
from dotenv import load_dotenv

# load API
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Connecting to bot
bot = telebot.TeleBot(API_KEY,parse_mode='MARKDOWN')

# Function to reply command
@bot.message_handler(commands=['Hello'])
def hello(message):
     bot.reply_to(message, "Hi, im a Monitoring bot v1")

# Start & Help Command
@bot.message_handler(commands=['start','help'])
def help(message):
    msg = '''
Monitoring Bot (Version 0.0.1)
---------
List Command Telegram Bot
1. Server information => /server
2. Bot Status => /status
3. Display all-mountpoint => /df
4. CPU and RAM Usage => /sysinfo
5. Show linux process => /top
6. Server Uptime => /uptime
7. get storage report => /getstorage
Help => /help

Regards,
Bots
---------
    '''
    bot.send_message(message.chat.id, msg)

# function bot status
@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, "Bot is Online")

import psutil
from psutil._common import bytes2human
import subprocess

# declare server desc (/server)
@bot.message_handler(commands=['server'])
def server(message):
    uname = subprocess.check_output(['lsb_release','-a']).decode('UTF-8')
    host = subprocess.check_output(['hostname']).decode('UTF-8')
    ipAddr = subprocess.check_output(['hostname','-I']).decode('UTF-8')
    msg ='''
```
Server Description
---------
Sistem Operasi
{}
Hostname
{}
IP Address
{}```'''.format(uname,host,ipAddr)
    bot.send_message(message.chat.id,msg)

# declare df -kh function (/df)
@bot.message_handler(commands=['df'])
def df(message):
    df = subprocess.check_output(['df','-kh']).decode('UTF-8')
    msg ='''
```
storage info
---------
{}
```'''.format(df)
    bot.send_message(message.chat.id,msg)

# cpu and ram info /sysinfo
@bot.message_handler(commands=['sysinfo'])
def sysinfo(message):
    cpuUsage = psutil.cpu_percent(interval=1)
    ramTotal = int(psutil.virtual_memory().total/(1024*1024)) #GB
    ramUsage = int(psutil.virtual_memory().used/(1024*1024)) #GB
    ramFree = int(psutil.virtual_memory().free/(1024*1024)) #GB
    ramUsagePercent = psutil.virtual_memory().percent
    msg = '''
```
CPU & RAM Info
---------
CPU Usage = {} %
RAM Usage
Total = {} MB
Usage = {} MB
Free  = {} MB
Used = {} %\n
```'''.format(cpuUsage,ramTotal,ramUsage,ramFree,ramUsagePercent)
    bot.send_message(message.chat.id,msg)

# show linux process /top
@bot.message_handler(commands=['top'])
def top(message):
    top = subprocess.check_output("top -b -n 1 | head -n 15", shell=True).decode('UTF-8')
    msg ='''
```
Linux Process :
---------
{}```'''.format(top)
    bot.send_message(message.chat.id,msg)

# uptime server /uptime
@bot.message_handler(commands=['uptime'])
def uptime(message):
    uptime = subprocess.check_output("uptime -p", shell=True).decode('UTF-8')
    msg ='''
Uptime Server :
---------
{}'''.format(uptime)
    bot.send_message(message.chat.id,msg)

bot.polling()
