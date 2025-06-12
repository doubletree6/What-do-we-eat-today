
import random
import datetime
import requests
import json
from os import environ
from json import dumps
from requests import post

def dishes():
    token = environ.get('token')
    if not token:
        # If the token is not present, stop sending push notification
        return 'PushPlus: No token configured, cannot send push notification.'
    url = 'http://www.pushplus.plus/send/'
    # List of dishes
    dishes = ["自助", "茶香鸡米饭", "羊汤", "泡馍", "拉面", "水饺", "BONUS TIME！", "炒菜", "鸡公煲", "板面", "冒菜", "馄饨", "炸串", "牛杂面", "炒饭", "烤鸭饭"]
    afternoon_dishes = ["沙拉", "炸串", "牛杂面"]

    current_hour = datetime.datetime.now().hour
    if current_hour < 6:
        dishes = [dish for dish in dishes if dish not in afternoon_dishes]

    # Randomly choose a dish from list
    chosen_dish = random.choice(dishes)

    data = {
        "token": token,
        "title": "这顿吃 " + chosen_dish",
        "content": "这顿吃 " + chosen_dish,
    }

    headers = {'Content-Type': 'application/json'}
    rsp = requests.post(url, data=json.dumps(data), headers=headers)
    return rsp.text

if __name__ == '__main__':
    print(dishes())
