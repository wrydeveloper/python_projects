from wxpy import *
import threading
import requests
import json,random
import sys
import datetime
import time

bot = Bot(console_qr=2,cache_path="botoo.pkl")
temp_dict = []
name = sys.argv[1]
setHour = 22
setMin = 30

def get_content(urls):
    html = requests.get(url=urls)
    return html.json()

def get_local_msg(filepath):

    with open(filepath, 'r') as file:
        loveword_dict = json.load(file)

    dict_len = len(loveword_dict)
    #随机数
    index_num = random.randint(0, int(dict_len)-1)

    if len(temp_dict) != 0 and len(temp_dict) != len(loveword_dict):
        for i in range(len(temp_dict)):
            if index_num in temp_dict:
                index_num = random.randint(0, int(dict_len)-1)
            else:
                temp_dict.append(index_num)
                break
    elif len(temp_dict) == len(loveword_dict):
        temp_dict[:] = []
    else:
        temp_dict.append(index_num)
    return loveword_dict[index_num]['content']


def send_one_msg():
    try:

        filepath = './loveword.json'
        content = get_local_msg(filepath)

        #你要发送的微信好友的昵称
        my_friend = bot.friends().search(name)[0]
        my_friend.send(content)

        t = threading.Timer(10, send_one_msg)
        t.start()

    except:
        my_friend = bot.friends().search('木头人')[0]
        my_friend.send(u"今天消息发送失败了")


if __name__ == "__main__":
    while True:
        while True:
            nowdate = datetime.datetime.now()
            if nowdate.hour == setHour and nowdate.minute == setMin:
                break
            time.sleep(20)
        send_one_msg()
        break



