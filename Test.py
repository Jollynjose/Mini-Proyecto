# from Card import *
# from Deck import *
# from constants import *
# from Table import *
# class Union:
#     def __init__(self):
#         self.union = []
#         self.value = self.total(self.cards)
        
#     def list_union(self,card):
#         self.union.append(card)
    

#     def clean(self,card):
#         return False
#     def ca(self):
#         t = 0
#         if self.union[-1] > self.value or self.union[-1] < self.value:
#             t = self.union [-1]
#             self.union = list(filter(self.cleanvalue,self.union))
#         self.union.append(self.value)
    
#     def cleanvalue(self,card):
#         if card > self.union[-1] or card < self.union[-1]:
#             return False
#         else:
#             return True


            

    #     c = list(filter(lambda v: v[1] != self.value, cards))
    #     if len(c) == 0:
    #         for card in cards:
    #             self.cards.append(card)
    #         return True

    #     newCardsTotal = self.total(cards)
    #     if newCardsTotal == self.value:
    #         for card in cards:
    #             self.cards.append(card)
    #         return True

    #     return False     

               
   

    # def total(self,cards):
    #     t = 0
    #     for card in self.cards:
    #             t = card[1] + t   
    #     return t

   
# cards = Cards(Values, Suits)
# deck = Deck(cards.card())
# Game = deck.initialize()
# c = []
# t = []
# for x in range(4):
#     c.append(Game.pop(2))
#     t.append(Game.pop(8))


def po(card):
    c = [1,2,3,4,5]
    for x in c:
        card.append(c)
    return c 

p= []
p = list(map(po,p))
print(p)