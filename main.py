#Sam, Davis, Nolan, Brett
from Player import Player
from cards import cards
from deck import deck

print("Welcome to Two-Deck War! Lets fight!")
player1 = Player(input("Player 1, what is your name? "))
player2 = Player(input("Player 2, what is your name? "))

deck1 = deck(card1)
deck2 = deck(card2)

#while both decks have card count > 0
    #first card in deckarray1 into compare variables, remove from deckarray1
    #first card in deckarray2 into compare variables, remove from deckarray2
    #compare the compare variables
    #if outright win
        #compare variables into loot array
        #clear compare variables (possibly optional)
        #put cards in deck array of winner all of the cards in loot array
        #clear loot array
    #else tie
        #put cards in compare variables into loot array
        #check to see if there are enough cards to put into the loot array (>= 4), if not, give all cards to other player and break
        #put next three cards in deckarray1 into loot array
        #put next three cards in deckarray2 into loot array

#congrats {winner} with not 0 cards