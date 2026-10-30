from deck import Deck

class Player:

    def __init__ (self, name):
        self.name = name
        self.deck = Deck()
        self.deck.shuffle()

    #Get the top card and remove it from the deck
    def draw_top_card(self):
        top_card = self.deck.cards.pop(0)
        #take the top card off of the player's deck (remove it from the deck)
        #and then return that top card
        return top_card

    #put the cards from loot into the winner's deck
    def append_deck(self, loot):
        for i in loot:
            self.deck.cards.append(i)
        loot.clear()

    #show how many cards the deck has
    def deck_count(self):
        count = len(self.deck.cards)
        return count