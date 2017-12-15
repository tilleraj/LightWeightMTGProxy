#! /usr/bin/env python3
import json
import pathlib
import csv
import sys

import cairo

import layout
from draw_card import drawCard
from card_model import CardModel

if len(sys.argv ) < 2:
    print('Error: No file specified')
    exit(1)

nameList = []

with open(sys.argv[1]) as csvFile:
    reader = csv.reader(csvFile)
    reader.__next__()
    for row in reader:
        nameList = nameList + [row[1]] * int(row[0])

cardList = [CardModel(name) for name in nameList]
pageList = [cardList[i:i+9] for i in range(0, len(cardList), 9)]

for page_number in range(len(pageList)):
    print(f'Page {page_number}:')
    page = pageList[page_number]
    surf = layout.getSurface()
    ctx = cairo.Context(surf)

    for i in range(len(page)):
        card = page[i]
        cardPos = (i % 3, i // 3)
        print(cardPos)
        print(card)
        mat = layout.getMatrix(*cardPos, surf)
        ctx.set_matrix(mat)
        drawCard(card, ctx)

    surf.write_to_png(f'page_{page_number}.png')

