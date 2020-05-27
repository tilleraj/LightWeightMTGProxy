import cairo
import card_model
import layout
import math


def showWrappedText(
    ctx: cairo.Context,
    text: str,
    top=0.0,
    left=0.0,
    right=None,
    lineHeight=12.0
):
    maxWidth = right - left
    inputLines = text.split('\n')
    inputWords = [line.split(' ') for line in inputLines]

    spacingInsideParagraphs = 1
    spaceBetweenParagraphs = 1.5

    totalLetters = 0
    numNewLines = len(inputWords)-1
    for line in inputWords:
        for word in line:
            # totalLetters += len(word)
            for char in word:
                if char.isalnum():
                    totalLetters += 1
    # charCap = 485
    charCap = 425
    newLineCharWeight = 50
    if totalLetters+(numNewLines*newLineCharWeight) > charCap:
        origLineHeight = lineHeight
        origExtraSpace = spaceBetweenParagraphs-1
        pctOverCap = (totalLetters+(numNewLines*newLineCharWeight))/charCap-1
        pctOverCap = math.sqrt(pctOverCap*100)/30


        # Reduce space between paragraphs
        newExtraSpace = origExtraSpace*(1-pctOverCap)
        spaceBetweenParagraphs = 1+newExtraSpace
        # Reduce font size
        newFontSize = origLineHeight * (1-pctOverCap)
        ctx.set_font_size(newFontSize)

        # Reduce lineHeight
        lineHeight = origLineHeight * (1-pctOverCap)

        linePct = "%.2f" % (100*(1-lineHeight/origLineHeight))
        fontPct = "%.2f" % (100*(1-newFontSize/origLineHeight))
        parPct = "%.2f" % (100*(1-newExtraSpace/origExtraSpace))

        print(f'{totalLetters} letters + {numNewLines} new lines was too big to fit.\n * lineHeight reduced {linePct}% from {origLineHeight} to {lineHeight}\n * fontSize reduced {fontPct}% from {origLineHeight} to {newFontSize}\n * paragraphSpacing reduced {parPct}% from {origExtraSpace} to {newExtraSpace}')
    print(f'{totalLetters}+{numNewLines}*{newLineCharWeight} = {totalLetters+numNewLines*newLineCharWeight}')
    print(numNewLines)

    currentOffset = 0

    for line in inputWords:
        currentLine = []

        while len(line):
            nextWord = line.pop(0)
            nextLine = currentLine + [nextWord]

            # If adding the next word would make the line go over the max width
            # Then start a new line
            if (ctx.text_extents(' '.join(nextLine)).width > maxWidth):
                ctx.move_to(left, top + currentOffset)
                ctx.show_text(' '.join(currentLine))
                currentLine = [nextWord]
                currentOffset = currentOffset + lineHeight*spacingInsideParagraphs
            else:
                currentLine = nextLine

        if (len(currentLine)):
            ctx.move_to(left, top + currentOffset)
            ctx.show_text(' '.join(currentLine))
            # Spacing between paragraphs
            currentOffset = currentOffset + lineHeight * spaceBetweenParagraphs


def drawCard(card: card_model.CardModel, ctx: cairo.Context):
    ctx.select_font_face('serif')

    # Draw name
    ctx.set_font_size(layout.nameH)
    ctx.move_to(*layout.nameBL)
    ctx.show_text(card.nameStr)

    # Draw type
    ctx.set_font_size(layout.typeH)
    ctx.move_to(*layout.typeBL)
    ctx.show_text(card.typeStr)

    # Draw cardText
    ctx.set_font_size(layout.cardTextH)
    showWrappedText(ctx, card.cardText,
                    top=layout.cardTextBL[1],
                    left=layout.cardTextBL[0],
                    right=layout.cardTextBL[0] + layout.cardTextW,
                    lineHeight=layout.cardTextH
                    )

    # Draw power/toughness
    if card.power is not None:
        ptStr = str(card.power) + '/' + str(card.toughness)
        ctx.set_font_size(layout.ptH)
        ctx.move_to(*layout.ptBL)
        ctx.show_text(ptStr)

    # Draw Loyalty
    if card.loyalty is not None:
        ptStr = " " + str(card.loyalty) + " "
        ctx.set_font_size(layout.ptH)
        ctx.move_to(*layout.loyaltyBL)
        ctx.show_text(ptStr)

    # Draw Mana Cost
    ctx.set_font_size(layout.nameH)
    ctx.move_to(
        layout.manaRight - ctx.text_extents(card.manaCost).width,
        layout.nameBL[1]
    )
    ctx.show_text(card.manaCost)
