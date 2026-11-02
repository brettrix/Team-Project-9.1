class Card:
    values = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
              "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        return Card.values[self.rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
