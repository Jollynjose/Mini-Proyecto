from constant import *
import random
# num_players = int(input('how much players going to play?  '))
class Game: 
    def __init__(self,deck):
        self.deck = deck 
        self.player1 = []
        self.player2 = []
        self.table= []
        self.game_deck = []
    def shuffle(self):
        self.game_deck= []
        for x in self.deck:
            self.game_deck.append(x)
        random.shuffle(self.game_deck)
    def deal_cards(self):
        while self.game_deck:
            if len(self.player1) < 4 and len(self.player2) < 4:
                self.player1.append(self.game_deck.pop())
                self.player2.append(self.game_deck.pop())
            else:
                break
    def game_table(self):
        while self.game_deck:
            if len(self.table) == 4:
                break
            else:
                self.table.append(self.game_deck.pop())

class Deck: 
    def __init__(self,cards):
        self.cards = cards
    def total_cards(self): #todas las cartas que lleva un deck
        return self.cards 
    def each_card(self): # Cada carta organizada en por su Suits
        Clubs= []
        Diamonds = []
        Hearts = []
        Spades = []
        for x in self.cards:
            if "Club" in x:
                Clubs.append(x)
            elif "Diamond" in x:
                Diamonds.append(x)
            elif "Heart" in x :
                Hearts.append(x)
            else:
                Spades.append(x)
        return Clubs, Diamonds, Hearts, Spades
    
        
class Cards:
    def __init__(self,Values,Suits): # Lo que tiene una carta
        self.Values = Values
        self.Suits = Suits
    def cards(self): #Creación de cartas
       deck = []
       for value in self.Values:
           for suit in self.Suits:
               deck.append(suit + ' - {} ' .format(value) )
       return deck

cards = Cards(Values,Suits)
deck = Deck(cards.cards())

Newgame = Game(deck.total_cards())













    

    



