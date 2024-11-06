"""
Todo:
    - Move classes and functions to their file
    - Improve UI
    - Optimize if else statements
"""

import random

#import functions
#import models

class player:
    def __init__(self, name, cards, wonpile):
        self.name = name
        self.cards = cards
        self.wonpile = wonpile

deck = []
for i in range(2, 15):
    for x in range(4):
        deck.append(i)

random.shuffle(deck)

user_input = input(f"Select your opponent: 'computer' or a 'friend'? ")

player1 = player(name = input("Add Player 1 Name: "), cards = deck[:26], wonpile = 0)
match user_input:
    case 'computer':
        player2 = player(name = 'Computer', cards = deck[26:], wonpile = 0)
    case 'friend':
        player2 = player(name = input('Add Player 2 Name: '), cards = deck[26:], wonpile = 0)
    case _:
        print("Wrong Input please select either 'computer' or 'friend'")

print(f"The deck has been shuffled and you have {len(player1.cards)} cards\n Good Luck!")

def game(player1, player2):
    index = 0
    while index < len(player1.cards) or index < len(player2.cards):
        user_action = input("Are you 'ready' to draw your cards: ")
        match user_action:
            case 'ready':
                print('-.....-')
                if player1.cards[index] > player2.cards[index]:
                    player1.wonpile += 2
                    print(f"Great, {player1.name}, you won this round")
                    # Remove one card for a regular comparison
                    player1.cards.pop(index)
                    player2.cards.pop(index)
                elif player1.cards[index] < player2.cards[index]:
                    player2.wonpile += 2
                    print(f"Ohh, {player1.name}, you lost this round")
                    # Remove one card for a regular comparison
                    player1.cards.pop(index)
                    player2.cards.pop(index)
                else:
                    print(f"{player1.name} your cards are equal.\nYou are going to WAR")
                    # Determine the number of cards to draw for "war" (e.g., 4)
                    num_cards_for_war = min(4, len(player1.cards) - index, len(player2.cards) - index)
                    if num_cards_for_war >= 4:
                        # Draw additional cards for "war" comparison
                        if player1.cards[index + 3] > player2.cards[index + 3]:
                            player1.wonpile += 8
                            print(f"Great, {player1.name}, you won this round")
                        elif player1.cards[index + 3] < player2.cards[index + 3]:
                            player2.wonpile += 8
                            print(f"Ohh, {player2.name}, you lost this round")
                        else:
                            temp_wonpile = 8
                            while player1.cards[index] == player2.cards[index]:
                                print(f"{player1.name} your cards are equal, draw 1 more")
                                index += 1
                                temp_wonpile += 1
                                if player1.cards[index] > player2.cards[index]:
                                    player1.wonpile += temp_wonpile
                                    break
                                elif player1.cards[index] < player2.cards[index]:
                                    player2.wonpile += temp_wonpile
                                    break

                        # Remove cards used in "war" from each player
                        for _ in range(num_cards_for_war):
                            player1.cards.pop(index)
                            player2.cards.pop(index)
                    else:
                        # Handle cases where not enough cards are left
                        print("It's your last card, good luck")
                        if player1.cards[index] > player2.cards[index]:
                            player1.wonpile += 2
                        elif player1.cards[index] < player2.cards[index]:
                            player2.wonpile += 2
                        # Remove last card if only one is left
                        player1.cards.pop(index)
                        player2.cards.pop(index)

                print(f"You have {player1.wonpile} cards in your won pile")
                print(f"You have {len(player1.cards)} cards remaining")
                print('-..........-')

            case _:
                print("Wrong input, try again -- To draw a card, type 'ready'")

    return player1, player2


playing = game(player1, player2)

if player1.wonpile > player2.wonpile:
    print(f"{player1.name} won with {player1.wonpile} while {player2.name} lost with {player2.wonpile} the card diference was {player1.wonpile - player2.wonpile}")
elif player1.wonpile < player2.wonpile:
    print(f"{player2.name} won with {player2.wonpile} while {player1.name} lost with {player1.wonpile} the card diference was {player2.wonpile - player1.wonpile}")
else:
    print(f"The game ended with a Tie and {player1.name} have collected equall amount of cards with {player2.name}")