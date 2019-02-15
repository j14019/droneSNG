# coding: utf-8
from slackbot.bot import Bot
from slackbot.bot import respond_to

import drone1
import ic_module

from pyparrot.Minidrone import Mambo

@respond_to('実行')
def now(message):

    drone1.a_func()
    ic_module.a_func()
    message.reply('結果が出ました')
    f = open('/home/pi/pyparrot/kekka.txt')
    data1 = f.read()
    message.reply(data1)
    f.close()

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print('KM:SlackBotを開始します!!!')
    main()
