import random 
# Deck class
class Deck: 
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

#List of possible cards
    def __init__(self):
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks: 
                card = f"{rank} of {suit}"
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

