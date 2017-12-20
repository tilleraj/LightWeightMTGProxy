# LightWeightMTGProxy
Generating lightweight proxies for playtesting Magic: The Gathering


## Description
This project came from a desire for a quick, easy, simple, and cheap way to print proxy cards at home for Magic: The Gathering.

Many of the tools found online at the time were based on high-res scans and the ones that weren't looked nothing like magic cards.

Our goal was to have something in the middle, a card that looked and felt familiar but was obviously not real and didn't use up all your ink.

The project accepts deck lists in the form of CSV's. It ignores the top line and assumes the first two columns are Quantity and Card Name respectively.

## Getting Started
Basically, all that is required to run is [Python 3.6](https://www.python.org/) (Yes, actually 3.6 or newer; 3.5 will not work.) and [PyCairo](https://cairographics.org/pycairo/). Depending on how you may use Python for other things, there are a few options for getting those installed. The instructions below are intended to be as simple as possible.

### Windows
- Download and install Python 3 using [the installer](https://www.python.org/downloads/windows/).
- Download this precompiled PyCairo [wheel file](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo).
- Run `pip install path\to\wheel_file.whl` to install PyCairo in a shell.
- Make a .csv deck list and run `python path\to\LightWeighMTGProxy\main.py my_decklist.csv`

### MacOS
- Install [Homebrew](https://brew.sh/) if you haven't already.
- Install Python 3 using `brew install python3` or upgrade it to the latest version.
- Install PyCairo using `pip3 install PyCairo`.
- Make a .csv deck list and run `python path/to/LightWeighMTGProxy/main.py my_decklist.csv`

## Sources and Documentation
### Card Text
The text layout is done using PyCairo. You can find their documentation at the link below. The website is kind of a mess and this is the one you want.
- Docs: https://pycairo.readthedocs.io/en/latest/

Any and all praise for card copy should go to people behind MTGJSON. They made this project infinitely easier by providing the "database" of all Magic cards in a nice clean file.
- Website: http://mtgjson.com/
- GitHub: http://github.com/mtgjson/mtgjson

### Images, .PSDs, and fonts
The source fils for making the layout images were gotten from the thread created by .Rai at Cardgame Coalition entitled "HD MtG Card Template: Deluxe Edition!"
- Thread: http://cardgamecoalition.forumotion.com/t789-hd-mtg-card-template-deluxe-edition

.Rai sites that his work is derivative of Pichoro at MTG Salvation. Based on the age of the .Rai's thread, I think the below is the thread he refers to.
- Thread: http://www.mtgsalvation.com/forums/community-forums/creativity/artwork/tutorials/341578-new-psd-links-thread-last-update-on-06-16-2012


## Legal
Official Statement from Elaine Chase, Vice President of Global Brand Strategy and Marketing for Wizards of the Coast (Jan 14, 2016)
https://magic.wizards.com/en/articles/archive/news/proxies-policy-and-communication-2016-01-14

### tl;dr
We aren't lawyers, but...

We aren't trying to make reproductions, we don't use official art, what we're producing wouldn't pass as the real thing, and WotC **IS OKAY** with this kind of behavior.

### Original Copy and Emphasis. (Edited for Brevity)
[L]et's clear things up.

**Our stated policy specifically applies to DCI-sanctioned events. Cards used in DCI-sanctioned events must be authentic *Magic* cards.** The only exception is if a card has become damaged during the course of play in a particular event.

**Our stance on counterfeits is also clear: Wizards remains committed to vigorously protecting the *Magic* community from counterfeiters.** [A]ny individual or retailer who knowingly deals in counterfeits works against the best interests of the community. Wizards has eliminated and will continue to eliminate from the DCI and WPN anyone who knowingly distributes counterfeit cards.

What has gotten caught up in the confusion are playtest cards used outside of sanctioned DCI events. 

A playtest card is most commonly a basic land with the name of a different card written on it with a marker. Playtest cards aren't trying to be reproductions of real *Magic* cards; they don't have official art and they wouldn't pass even as the real thing under the most cursory glance. Fans use playtest cards to test out new deck ideas before building out a deck for real and bringing it to a sanctioned tournament. And that's perfectly fine with us. **Wizards of the Coast has no desire to police playtest cards made for personal, non-commercial use, even if that usage takes place in a store.**

What we really care about is that DCI-sanctioned events use only authentic *Magic* cards, and that we stop counterfeits.
