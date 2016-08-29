import random

'''
Ranks: 2 3 4 5 6 7 8 9 10 J Q K A
Kind: D H C S
'''

class Card():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    values = {}
    #set the values of the ranks based on the order of the ranks in the list above.
    for index, val in enumerate(ranks):
        values[index] = val
    kinds = ['D', 'H', 'C', 'S']
    englishRanks = {'J':'Jack', 'Q':'Queen', 'K':'King', 'A':'Ace'}
    englishKinds = {'D':'Diamonds', 'H':'Hearts', 'C':'Clubs', 'S':'Spades'}
    def __init__(self, rank, kind):
        if rank in Card.ranks:
            self.rank = rank
        else:
            print("Tried to set impossible rank: {}".format(rank))
        if kind in Card.kinds:
            self.kind = kind
        else:
            print("Tried to set impossible kind: {}".format(kind))

    def __str__(self):
        #if it needs an English translation, get it, else use its normal form.
        return "{} of {}".format(Card.englishRanks[self.rank] if self.rank in Card.englishRanks else self.rank, 
        Card.englishKinds[self.kind] if self.kind in Card.englishKinds else self.kind)
          

class Deck():
    def __init__(self, initWith = None, shuffle = True):
        if initWith!=None: #set up deck with given cards
            self._deck = initWith[:]
        else: #set up full deck of cards
            self._deck = [Card(rank, kind) for rank in Card.ranks for kind in Card.kinds] #make a deck with all the cards in it.
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self._deck)
        
    def draw(self):
        if len(self._deck)>0:
            return self._deck.pop()
        else:
            return None
    
    def addCards(self, listOfCards):
        self._deck.extend(listOfCards)
     
    #returns how many cards there are left in the deck   
    def size(self):
        return len(self._deck)


print(Card.values)