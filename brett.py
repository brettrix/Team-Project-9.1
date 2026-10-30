
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

from Player import Player

Player1 = Player("Player1")
Player2 = Player("Player2")

loot = ["3 of spades", "8 of diamonds", "Queen of hearts"]

print(Player1.deck_count())
Player1.draw_top_card()
print(Player1.deck_count())
Player1.append_deck(loot)
print(Player1.deck_count())