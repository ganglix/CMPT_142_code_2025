import random

name_list = [
    "Calla", "Logan", "Marc", "Fletcher", "Joshua",
    "Marl", "Gang", "Logan", "Barney", "Jessika",
    "Kale", "Rhett", "Kartik"
]
emoji_list = ["\U0001F600", "\U0001F602", "\U0001F605", "\U0001F609", "\U0001F914", "\U0001F60E"]
name = random.choice(name_list)
emoji = random.choice(emoji_list)

print(emoji, name)

