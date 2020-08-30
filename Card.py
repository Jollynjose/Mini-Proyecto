from constants import *
import random
# num_players = int(input('how much players going to play?  '))
class Cards:
    def __init__(self,Values,Suits): # Lo que tiene una carta
        self.Values = Values
        self.Suits = Suits
    def cards(self): #Creación de cartas
       deck = []
       for value in self.Values:
           for suit in self.Suits:
               deck.append([suit,value])
       return deck
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
    

class properties_of_cards: 
    def __init__(self,deck):
        self.deck = deck 
        self.player1 = []
        self.player2 = []
        self.table= []
        self.game_deck = []
        self.playerturn = 1
    def shuffle_card(self):
        c = []
        for x in self.deck:
            c.append(x)
        random.shuffle(c)
        for y in c:
            self.game_deck.append(u)
        return self.game_table

    def deal_cards(self):
        count = 0
        for x in range(len(self.game_deck)):
            if self.game_deck:
                if count == 4:
                    break
                self.player1.append(self.game_deck[x])
                del self.game_deck[x]
                self.player2.append(self.game_deck[x])
                del self.game_deck[x]
            else:
                break
            count = count + 1

    def game_table(self):
        for x in range(4):
            self.table.append(self.game_deck.pop())
        return self.table
    def turn(self):
        if self.playerturn == 1:
            self.playerturn = 0
        else:
            self.playerturn = 1 
        return self.playerturn
class Player:
    def __init__(self,name,mazo):
        self.name = name
        self.mazo = mazo
        self.deck = [] #TODO: search a better name
    def __str__(self):
        return self.name, self.mazo, self.deck

        
        
cards = Cards(Values,Suits)
deck = Deck(cards.cards())
properties = properties_of_cards(deck.total_cards())

# player1 = Player(' {} - Player 1'.format(input("Escriba su nombre Jugador 1 : " )), propieties.player1)
# player2 = Player(' {} - Player 2'.format(input("Escriba su nombre Jugador 2 : " )), propieties.player2)
player1 = Player('Peter', properties.player1)
player2 = Player('jimmy', properties.player2)



