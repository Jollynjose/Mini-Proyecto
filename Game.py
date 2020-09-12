import random
from Table import *
from Player import *
class Game_of_two:
    def __init__(self, deck):
        self.deck = deck
        
        
    def shuffle_cards(self):
        shuffle = []
        shuffle = self.deck
        random.shuffle(shuffle)
        return shuffle

    def create_table(self):
        table = Table()
        for x in range(4):
            table.cards.append(self.deck.pop())
        return table

    def players_deck_of_card(self,card):
        for x in range(4):
            if self.deck:
                card.append(self.deck.pop())
            else:
                break
        

    def calculate_points(self,player):
        playerpoints = 0
        total_cards = len(player)
        cards_spades = 0
        for x in range(len(player)):
            if player[x][1] == 1:
                playerpoints = playerpoints + 1
            elif player[x][0] == 'Diamond' and player[x][1] == 10:
                playerpoints = playerpoints + 2
            elif player[x][0] == 'Spade' and player[x][1] == 2:
                playerpoints = playerpoints + 1
            elif player[x][0] == 'Spade':
                cards_spades = cards_spades + 1

        return playerpoints, total_cards, cards_spades

    def check_winner(self,player_One,player_Two):
        points_playerOne, more_cards_playerOne, player_One_Spades = self.calculate_points(player_One.deck_of_cards_grabbed)
        points_playerTwo, more_cards_playerTwo, player_Two_Spades = self.calculate_points(player_Two.deck_of_cards_grabbed)
        if more_cards_playerOne > more_cards_playerTwo:
            points_playerOne = points_playerOne + 3
        elif more_cards_playerOne < more_cards_playerTwo:
            points_playerTwo = points_playerTwo + 3
        if player_One_Spades > player_Two_Spades:
            points_playerOne = points_playerOne + 1
        elif player_One_Spades < player_Two_Spades:
            points_playerTwo = points_playerTwo + 1
       

        if points_playerOne > points_playerTwo:
            return 'Player 1 {} has won with {} Points'.format(player_One.name,points_playerOne)
        elif points_playerOne == points_playerTwo:
            return 'Player 1 {} and Player 2 {} have a tie '.format(player_One.name,player_Two.name)
        elif points_playerOne < points_playerTwo:
            return 'Player 2 {} has won with {} Points'.format(player_Two.name,points_playerTwo)       

        
    
        
        