import json
import pathlib

cardDb = dict()
with open(pathlib.Path(__file__).parent / 'AllCards.json', encoding='utf-8') as dbFile:
    db = json.load(dbFile)

class CardModel:
    def __init__(self, name=None):
        self.nameStr = "NAME"
        self.typeStr = "TYPE - SUBTYPE"
        self.cardText = "Some text"
        self.manaCost = "\{W\}"
        self.power = None
        self.toughness = None
        self.loyalty = None

        if (name is not None):
            self.load(db[name])

    def load(self, data: dict):
        self.nameStr = data['name']
        self.typeStr = data['type']

        if ('text' in data):
            self.cardText = data['text']
        else:
            self.cardText = ""
        
        if ('manaCost' in data):
            self.manaCost = data['manaCost']
        else:
            self.manaCost = ""
        
        if 'power' in data:
            self.power = int(data['power'])
            self.toughness = int(data['toughness'])
        
        if 'loyalty' in data:
            self.loyalty = int(data['loyalty'])

    def __str__(self):
        return f'{self.nameStr} - {self.manaCost} ({self.typeStr})'