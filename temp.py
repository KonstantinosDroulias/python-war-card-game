"""
This is the function I wrote for my test program
'I couldn't make more cards to be removed from my list when the user was going to war
'So I used chatgpt to help me with that part... Now the part chatgpt wrote sits on the main.py
"""

def game(player1, player2):
    while index < len(player1.cards) or index < len(player2.cards):
        #Till I check everything works
        user_action = input("Are you 'ready' to draw your cards: ")
        match user_action:
            case 'r':
                print('-.....-')
                if player1.cards[index] > player2.cards[index]:
                    player1.wonpile += 2
                    print(f"Great, {player1.name}, you won this round")

                    player1.cards.pop(index)
                    player2.cards.pop(index)
                elif player1.cards[index] < player2.cards[index]:
                    player2.wonpile += 2
                    print(f"Ohh, {player1.name}, you lost this round")

                    player1.cards.pop(index)
                    player2.cards.pop(index)
                else:
                    print(f"{player1.name} your cards are equal.\nYou are going to WAR")
                    if (index + 3) < len(player1.cards) or (index + 3) < len(player2.cards):
                        if player1.cards[index + 3] > player2.cards[index + 3]:
                            player1.wonpile += 8
                            print(f"Great, {player1.name}, you won this round")
                            index = index + 3

                            player1.cards.pop(index + 3)
                            player2.cards.pop(index + 3)
                        elif player1.cards[index + 3] < player2.cards[index + 3]:
                            player2.wonpile += 8
                            print(f"Ohh, {player2.name}, you lost this round")
                            index = index + 3

                            player1.cards.pop(index + 3)
                            player2.cards.pop(index + 3)
                        else:
                            index = index + 3
                            temp_wonpile = 8
                            
                            player1.cards.pop(index)
                            player2.cards.pop(index)
                            while player1.cards[index] == player2.cards[index]:
                                print(f"{player1.name} your cards are equal draw 1 more")
                                index = index + 1
                                temp_wonpile = temp_wonpile + 1
                                
                                player1.cards.pop(index)
                                player2.cards.pop(index)
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

                            player1.cards.pop(index)
                            player2.cards.pop(index)
                        elif player1.cards[index + 2] < player2.cards[index + 2]:
                            player2.wonpile += 6
                            print(f"Ohh, {player2.name}, you lost this round")
                            index = index + 2

                            player1.cards.pop(index)
                            player2.cards.pop(index)
                        else:
                            index = index + 2
                            temp_wonpile = 6
                            
                            player1.cards.pop(index)
                            player2.cards.pop(index)
                            while player1.cards[index] == player2.cards[index]:
                                print(f"{player1.name} your cards are equal draw 1 more")
                                index = index + 1
                                temp_wonpile = temp_wonpile + 1
                                
                                player1.cards.pop(index)
                                player2.cards.pop(index)
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

                        player1.cards.pop(index)
                        player2.cards.pop(index)
                print(f"You have {player1.wonpile} cards in your won pile")
            
                        
                                
                # Remove the cards that were just compared
                
                print(f"You have {len(player1.cards)} cards remaining")
                print('-..........-')

            case _:
                print("Wrong input try again -- To draw a card type 'ready'")

    return player1, player2