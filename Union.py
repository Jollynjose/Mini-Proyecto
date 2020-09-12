from Table import *
class Union:
    def __init__(self):
        self.cards = Table().unions_on_table
        
    
    def add_card(self,cards):
            cards = list(filter(self.erase_value_in_card,cards))
            value = self.total(cards)
            cards.append(value)
            print(value)
            return cards
            

    def erase_value_in_card(self,card):
        c = str(card)
        if c.isdigit():
            return False
        return True

    def total(self,cards):
        t = 0
        if cards[0][1] == cards[1][1]:
            return cards[0][1]
        else:
            for card in cards:
                t = card[1] + t   
            return t
    
    

            