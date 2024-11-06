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
                elif player1.cards[index] < player2.cards[index]:
                    player2.wonpile += 2
                    print(f"Ohh, {player1.name}, you lost this round")
                else:
                    print(f"{player1.name} your cards are equal.\nYou are going to WAR")
                    if (index + 3) < len(player1.cards) or (index + 3) < len(player2.cards):
                        if player1.cards[index + 3] > player2.cards[index + 3]:
                            player1.wonpile += 8
                            print(f"Great, {player1.name}, you won this round")
                            index = index + 3
                        elif player1.cards[index + 3] < player2.cards[index + 3]:
                            player2.wonpile += 8
                            print(f"Ohh, {player2.name}, you lost this round")
                            index = index + 3
                        else:
                            index = index + 3
                            temp_wonpile = 8
                            
                            while player1.cards[index] == player2.cards[index]:
                                print(f"{player1.name} your cards are equal draw 1 more")
                                index = index + 1
                                temp_wonpile = temp_wonpile + 1
                                
                                if player1.cards[index] > player2.cards[index]:
                                    player1.wonpile += temp_wonpile
                                    
                                elif player1.cards[index] < player2.cards[index]:
                                    player2.wonpile += temp_wonpile
                                else:
                                    pass
                    elif (index + 2) < len(player1.cards) or (index + 2) < len(player2.cards):
                        if player1.cards[index + 2] > player2.cards[index + 2]:
                            player1.wonpile += 6
                            print(f"Great, {player1.name}, you won this round")
                            index = index + 2
                        elif player1.cards[index + 2] < player2.cards[index + 2]:
                            player2.wonpile += 6
                            print(f"Ohh, {player2.name}, you lost this round")
                            index = index + 2
                        else:
                            index = index + 2
                            temp_wonpile = 6
                            
                            while player1.cards[index] == player2.cards[index]:
                                print(f"{player1.name} your cards are equal draw 1 more")
                                index = index + 1
                                temp_wonpile = temp_wonpile + 1
                                
                                if player1.cards[index] > player2.cards[index]:
                                    player1.wonpile += temp_wonpile
                                    
                                elif player1.cards[index] < player2.cards[index]:
                                    player2.wonpile += temp_wonpile
                                else:
                                    pass
                    else:          
                        print("It's your last card, good luck")
                        if player1.cards[index] > player2.cards[index]:
                            player1.wonpile += 2
                            print(f"Great, {player1.name}, you won this round")
                            #index = index + 2
                        elif player1.cards[index] < player2.cards[index]:
                            player2.wonpile += 2
                            print(f"Ohh, {player2.name}, you lost this round")
                            #index = index + 2
                        else:
                            print("Your last cards are equal... The 2 cards are burned and noone wins them")

                print(f"You have {player1.wonpile} cards in your won pile")
            
                        
                                
                # Remove the cards that were just compared
                player1.cards.pop(index)
                player2.cards.pop(index)
                print(f"You have {len(player1.cards)} cards remaining")
                print('-..........-')

            case _:
                print("Wrong input try again -- To draw a card type 'ready'")

    return player1, player2


playing = game(player1, player2)

if player1.wonpile > player2.wonpile:
    print(f"{player1.name} won with {player1.wonpile} while {player2.name} lost with {player2.wonpile} the card diference was {player1.wonpile - player2.wonpile}")
elif player1.wonpile < player2.wonpile:
    print(f"{player2.name} won with {player2.wonpile} while {player1.name} lost with {player1.wonpile} the card diference was {player2.wonpile - player1.wonpile}")
else:
    print(f"The game ended with a Tie and {player1.name} have collected equall amount of cards with {player2.name}")