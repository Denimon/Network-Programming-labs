import random

cardValue = {
    1: 'Ace',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Jack',
    12: 'Queen',
    13: 'King'
}
cardSuit = {
    1: 'Spades',
    2: 'Hearts',
    3: 'Diamonds',
    4: 'Clubs'
}

class Card:
    def __init__(self, suit, value):
        assert 1 <= suit <= 4 and 1 <= value <= 13
        self._suit = suit
        self._value = value

    def getValue(self):
        return self._value

    def getSuit(self):
        return self._suit

    def __str__(self):
       return (cardSuit[self._suit] + ' of ' + cardValue[self._value])



class CardDeck:
    def __init__(self):
        self._deck = []
        self._deck = self.reset()
    

    def shuffle(self):
        random.shuffle(self._deck)

    def getCard(self):
        return self._deck.pop()


    def size(self):
        return len(self._deck)


    def reset(self):

        self._deck = []
        for i in range(1,5):
            for j in range(1,14):
                self._deck.append(Card(i,j))    
            
        
        return self._deck
        


deck = CardDeck()
deck.shuffle()

while deck.size()> 0:
    card = deck.getCard()
    print("Card {} has value {}".format(card, card.getValue()))
