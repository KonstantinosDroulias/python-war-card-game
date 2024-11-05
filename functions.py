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