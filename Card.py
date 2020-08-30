from constant import *
import random
class Deck: 
    def __init__(self,cards):
        self.cards = cards
    def create_deck(self): #todas las cartas que lleva un deck
        suits , values = self.cards
        deck = []
        for suit in suits:
            for value in values:
                deck.append([suit,value])
        return deck

class Cards:
    def __init__(self,Values,Suits): # Lo que tiene una carta
        self.Values = Values
        self.Suits = Suits
    def card(self):
        cards = self.Suits, self.Values
        return cards

class Game_of_two : 
    def __init__(self,deck):
        self.deck = deck 
    def shuffle_cards(self):
        shuffle = []
        shuffle = self.deck
        random.shuffle(shuffle)
        return shuffle
    def game_table(self):
        table = []
        for x in range(4):
            table.append(self.deck[x])
            del self.deck[x]
        return table
    def players_deck_of_card(self):
        player1 = []
        player2 = []
        for x in range(4):
            player1.append(self.deck[x])
            del self.deck[x]
            player2.append(self.deck[x])
            del self.deck[x]
        return player1, player2

class Player:
    def __init__(self,name,deck_of_cards):
        self.name = name
        self.deck_of_cards = deck_of_cards
        self.deck_of_cards_points = [] #Search a better name
    def __str__(self):
        return self.name, self.deck_of_cards , len(self.deck_of_cards_points)
        

        


cards = Cards(Values,Suits)
deck = Deck(cards.card())
Game = Game_of_two(deck.create_deck())
Game.shuffle_cards()
Game.game_table()
player1_deck_of_card , player2_deck_of_card = Game.players_deck_of_card()
player1 = Player("Jimmy",player1_deck_of_card)
player2 = Player('Peter',player2_deck_of_card)
print(player1.__str__())


