from constant import *
class Game: 
    def __init__(self,player1,player2,player3,player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
    
class Deck: 
    def __init__(self,cards):
        self.cards = cards
    def total_cards(self): #todas las cartas que lleva un deck
        return self.cards , "{} - cards deck".format(len(self.cards))
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

print(deck.total_cards())












    

    



