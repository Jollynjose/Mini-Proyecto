from constant import *
import random
class Game: 
    def __init__(self,deck):
        self.player1 = None
        self.player2 = None
        self.admin = []
        self.deck = deck 
    def shuffle(self):
        self.admin= []
        for x in self.deck:
            self.admin.append(x)
        random.shuffle(self.admin)
        return self.admin
    
    
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















    

    



