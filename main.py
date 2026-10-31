# Sam, Davis, Nolan, Brett
from Player import Player

print("Welcome to Two-Deck War! Lets fight!")

player1 = Player(input("Player 1, what is your name? "))
player2 = Player(input("Player 2, what is your name? "))

# Your Player class creates and shuffles each player's deck.
# Your current Deck stores cards as strings.
rank_values = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "Jack": 11, "Queen": 12,
    "King": 13, "Ace": 14
}

loot = []
war = False

while player1.deck_count() > 0 and player2.deck_count() > 0:
    # Draw and remove one card from each player's deck.
    card1 = player1.draw_top_card()
    card2 = player2.draw_top_card()

    print(f"\n{player1.name} drew the {card1}.")
    print(f"{player2.name} drew the {card2}.")

    # Extract the rank from strings such as "King of Hearts".
    rank1 = card1.split(" of ")[0]
    rank2 = card2.split(" of ")[0]

    value1 = rank_values[rank1]
    value2 = rank_values[rank2]

    # Preserve all cards played until there is a winner.
    loot.extend([card1, card2])

    if value1 > value2:
        player1.append_deck(loot)

        if war:
            print(f"{player1.name} wins the war!")
        else:
            print(f"{player1.name} wins the round!")

        war = False

    elif value2 > value1:
        player2.append_deck(loot)

        if war:
            print(f"{player2.name} wins the war!")
        else:
            print(f"{player2.name} wins the round!")

        war = False

    else:
        print("War!")
        war = True

        # Extra rule for running out of cards during a tie.
        if player1.deck_count() == 0 and player2.deck_count() == 0:
            print("Neither player has another card to continue the war.")
            break

        elif player1.deck_count() == 0:
            player2.append_deck(loot)
            print(f"{player1.name} cannot continue the war.")
            break

        elif player2.deck_count() == 0:
            player1.append_deck(loot)
            print(f"{player2.name} cannot continue the war.")
            break

        # Draw another comparison pair without clearing loot.
        continue

    # Display counts only after the round or war is resolved.
    print(f"{player1.name} has {player1.deck_count()} cards.")
    print(f"{player2.name} has {player2.deck_count()} cards.")

    if player1.deck_count() > 0 and player2.deck_count() > 0:
        input("Press Enter to play the next round.")

# Announce the final result.
if player1.deck_count() > 0:
    print(f"\n{player1.name} has collected all of the cards.")
    print(f"{player1.name} wins the game!")

elif player2.deck_count() > 0:
    print(f"\n{player2.name} has collected all of the cards.")
    print(f"{player2.name} wins the game!")

else:
    print("\nThe game ends in a draw.")