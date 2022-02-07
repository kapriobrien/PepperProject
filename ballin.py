import random
import requests
import json

unformattedCards = requests.get("https://deckofcardsapi.com/api/deck/v7qhzbwygz4k/draw/?count=1")
data = unformattedCards.text
cardParse = json.loads(data)

def drawCard():
    return cardParse["cards"][0]["value"]

def checkForShuffle():
    if(cardParse["remaining"] <=1):
        return requests.get("https://deckofcardsapi.com/api/deck/v7qhzbwygz4k/shuffle/")

print(drawCard())
