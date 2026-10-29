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
    else:#tie
        if len(deck1.cards) < 4:
            deck2.cards.extend(deck1.cards)
            deck1.cards.clear()
            deck2.cards.extend(loot)
            loot.clear()
            break
        elif len (deck2.cards) < 4:
            deck1.cards.extend(deck2.cards)
            deck2.cards.clear()
            deck1.cards.extend(loot)
            loot.clear()
            break
        for _ in range(3):
            loot.append(deck1.cards.pop(0))
            loot.append(deck2.cards.pop(0))
        #check to see if there are enough cards to put into the loot array (>= 4), if not, give all cards to other player and break
        #put next three cards in deckarray1 into loot array
        #put next three cards in deckarray2 into loot array

#congrats {winner} with not 0 cards