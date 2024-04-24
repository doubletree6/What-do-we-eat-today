import random
import datetime

# List of dishes
dishes = ["自助", "茶香鸡米饭", "羊汤", "泡馍", "拉面", "水饺", "BONUS TIME！", "炒菜", "鸡公煲", "板面", "冒菜", "馄饨", "炸串", "牛杂面", "炒饭"]

# Define afternoon dishes
afternoon_dishes = ["沙拉", "炸串", "牛杂面"]

# Get current hour
current_hour = datetime.datetime.now().hour

# If morning, remove afternoon dishes from the list
if current_hour < 12:
    dishes = [dish for dish in dishes if dish not in afternoon_dishes]

# Randomly choose a dish from list
chosen_dish = random.choice(dishes)

print("这顿吃 " + chosen_dish)