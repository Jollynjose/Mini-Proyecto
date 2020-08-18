class Decks: 
    def __init__(self,Values,Suits):
        self.Values= Values
        self.Suits= Suits
    def cards(self):
        return self.Values , self.Suits
class Cards(Decks):
    def card(self):
       value1 , suit1 = super().cards()
       deck = []
       for value in value1:
           for suit in suit1:
               deck.append(suit + ' - {} ' .format(value) )
       return deck
class player (Decks,Cards):
    pass
       
clubs = '♣'
diamonds = '♦'
hearts = '♥'
spades = '♠'
Values= [1,2,3,4,5,6,7,8,9,10,11,12,13]
Suits= [clubs,diamonds,hearts,spades]
Deck =  Cards(Values,Suits)
print(Deck.card())