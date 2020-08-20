from Card import *
from constant import*

cards = Cards(Values,Suits)
deck = Deck(cards.cards())
Newgame = Game(deck.total_cards())
Newgame.shuffle()
print(Newgame.admin)