import random
from Table import *

class Game_of_two:
    def __init__(self, deck):
        self.deck = deck
        self.playerOne = []
        self.playerTwo = []

    def shuffle_cards(self):
        shuffle = []
        shuffle = self.deck
        random.shuffle(shuffle)
        return shuffle

    def create_table(self):
        table = Table()
        for x in range(4):
            table.cards.append(self.deck[x])
            del self.deck[x]
        return table

    def players_deck_of_card(self):
        for x in range(4):
            self.playerOne.append(self.deck[x])
            del self.deck[x]
            self.playerTwo.append(self.deck[x])
            del self.deck[x]
        return self.playerOne, self.playerTwo