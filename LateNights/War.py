'''
Goal is to have me play war against a computer that just chooses any card at random.
'''

import BasicDeck as bd

fullDeck = bd.Deck()


decks = [[],[]]
extraDecks = [bd.Deck([]), bd.Deck([])]
hands = [[], []] #I could make a class for this, but I decided not to.
#assumes the deck has an even number of cards.
if fullDeck.size()%2!=0:
    print("Warning! Uneven deck will most likely not split correctly!")
while fullDeck.size()>0:
    for deck in decks:
        deck.append(fullDeck.draw())

for i, deck in enumerate(decks):
    decks[i] = bd.Deck(deck)


    