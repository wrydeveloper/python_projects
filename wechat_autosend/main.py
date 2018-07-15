from wxpy import *
from threading import Timer
import requests
import re
import threadpool
import time

bot = Bot(console_qr=2,cache_path="botoo.pkl")

def get_content(urls):
    html = requests.get(url=urls)
    return html.json()


def send_one_msg(name):
    try:
        url = 'http://open.iciba.com/dsapi/'
        content = get_content(url)
        #你要发送的微信好友的昵称
        my_friend = bot.friends().search(name)[0]
        my_friend.send(content['content'])
        my_friend.send(content['note'])
        my_friend.send(content['translation'])

    except:
        my_friend = bot.friends().search('木头人')[0]
        my_friend.send(u"今天消息发送失败了")

def send_many_msg(namelist):
    # namelist = ['{微信昵称}','{微信昵称}']
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(send_one_msg, namelist)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    
    t = Timer(1, send_many_msg(namelist))
    t.start()

if __name__ == "__main__":
    send_many_msg(['土亢', '我是猫'])


