#! /usr/bin/env python3
import csv
import json
import os
import pathlib
import sys

import cairo

import layout
from draw_card import drawCard
from card_model import CardModel

if len(sys.argv ) < 2:
    print('Error: No file specified')
    exit(1)

deck_file = sys.argv[1]
deck_name = os.path.basename(deck_file)[:-4]
nameList = []
list_copy = []

with open(deck_file, encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile)
    list_copy.append(reader.__next__())
    for row in reader:
        list_copy.append(row)
        nameList = nameList + [row[1]] * int(row[0])

cardList = [CardModel(name) for name in nameList]
pageList = [cardList[i:i+9] for i in range(0, len(cardList), 9)]

if not os.path.exists('decks'):
    os.mkdir('decks')
if not os.path.exists(os.path.join('decks',deck_name)):
    os.mkdir(os.path.join('decks',deck_name))

for page_number in range(len(pageList)):
    print(f'Page {page_number}:')
    page = pageList[page_number]
    surf = layout.getSurface()
    ctx = cairo.Context(surf)

    for i in range(len(page)):
        card = page[i]
        cardPos = (i % 3, i // 3)
        # print(cardPos)
        print(card)
        mat = layout.getMatrix(*cardPos, surf)
        ctx.set_matrix(mat)
        drawCard(card, ctx)

    surf.write_to_png(f'decks/{deck_name}/{deck_name}_p{page_number}.png')

with open(f'decks/{deck_name}/{deck_name}.csv', 'w') as deck_copy:
    filewriter = csv.writer(deck_copy)
    for element in list_copy:
        filewriter.writerow(element)