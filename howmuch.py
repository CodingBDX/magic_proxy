import requests
import re
import json
import os
import os.path
print ("what's name of file TXT ?")
answer2=input("enter your_file.txt =>")
path2 = os.path.dirname(os.path.realpath(__file__))
filePath2 = os.path.join(path2, answer2)
def request_url(name):
    name = name.replace(" ", "+")
    return f"https://api.scryfall.com/cards/search?q={name}&order=eur&dir=asc"

with open(r + "filePath2") as f:
    lines = f.read().split('\n')
    total_price = 0
    cards = {}
    for line in lines:
        amount, name = re.split(r"\s+", line, 1)
        resp = requests.get(request_url(name))
        data = json.loads(resp.content)
        if not resp.status_code == 200:
            print(f"Card {name} doesn't exist.")
            continue
        if data["data"][0]["prices"]["eur"]:
            price = float(data["data"][0]["prices"]["eur"]) * int(amount)
            cards[name] = (amount, price)
            total_price += price
        else:
            print(f"Price not found for {name}.")
    for name, value in cards.items():
        print(f'{value[0]} {name}: {round(value[1], 2)}€')
    print("Total: ", total_price, "€")