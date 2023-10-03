import os
import json
from dotenv import load_dotenv

load_dotenv()
CLASH_TOKEN = os.getenv("TOKEN")
cards = requests.get("https://royaleapi.github.io/cr-api-data/json/cards.json").json()
levels = requests.get(f"https://api.clashroyale.com/v1/players/{usertag}", headers={"Accept": "application/json", "Authorization": f"Bearer {CLASH_TOKEN}"}).json()["cards"]

def find_card(name):
    for card in cards:
        if name == card["name"]:
            for level in levels:
                if name == level["name"]:
                    if card["rarity"] == "Common":
                        rarityValue = 0 + level["level"]
                    elif card["rarity"] == "Rare":
                        rarityValue = 2 + level["level"]
                    elif card["rarity"] == "Epic":
                        rarityValue = 5 + level["level"]
                    elif card["rarity"] == "Legendary":
                        rarityValue = 8 + level["level"]
                    elif card["rarity"] == "Champion":
                        rarityValue = 10 + level["level"]
                    result = f"Card: {card['name']}\nLevel: {rarityValue}\nID: {card['key']} ({card['id']})\nElixir: {card['elixir']}\nType: {card['type']}\nRarity: {card['rarity']}\nArena: {card['arena']}\nAbout: {card['description']}"
            break
        else: result = "Not Found!"
    return result
print(find_card(input("Search: ")))
