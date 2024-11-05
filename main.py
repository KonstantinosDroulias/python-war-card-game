import random

#import functions
#import models

class player:
    def __init__(self, cards, wonpile):
        self.cards = cards
        self.wonpile = wonpile

deck = []
for i in range(2, 15):
    for x in range(4):
        deck.append(i)

random.shuffle(deck)

player1 = player(cards = deck[:26], wonpile = 0)
player2 = player(cards = deck[26:], wonpile = 0)
 
def game(player1, player2):
    index = 0
    while index < len(player1.cards) or index < len(player2.cards):
        if player1.cards[index] > player2.cards[index]:
            player1.wonpile += 2
        elif player1.cards[index] < player2.cards[index]:
            player2.wonpile += 2
        else:
            if player1.cards[index + 3] > player2.cards[index + 3]:
                player1.wonpile += 8
                index = index + 3
            elif player1.cards[index + 3] < player2.cards[index + 3]:
                player2.wonpile += 8
                index = index + 3
            else:
                index = index + 3
                temp_wonpile = 8
                while player1.cards[index] == player2.cards[index]:
                    index = index + 1
                    temp_wonpile = temp_wonpile + 1
                    if player1.cards[index] > player2.cards[index]:
                        player1.wonpile += temp_wonpile
                    elif player1.cards[index] < player2.cards[index]:
                        player2.wonpile += temp_wonpile
                    else:
                        pass
                
                        

        # Remove the cards that were just compared
        player1.cards.pop(index)
        player2.cards.pop(index)

        return player1, player2


playing = game(player1, player2)

if player1.wonpile > player2.wonpile:
    print(f"Player 1 won with {player1.wonpile} while player 2 lost with {player2.wonpile} the card diference was {player1.wonpile - player2.wonpile}")
elif player1.wonpile < player2.wonpile:
    print(f"Player 1 won with {player2.wonpile} while player 2 lost with {player1.wonpile} the card diference was {player2.wonpile - player1.wonpile}")
else:
    print(f"The game ended with a Tie and Player 1 and 2 have collected equall amount of cards")