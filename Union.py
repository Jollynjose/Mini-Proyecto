
class Union:
    def __init__(self):
        self.cards = []
        self.value = self.total(self.cards)
       
    
    def add_card(self,cards):
            cards = list(filter(self.erase_value_in_card,cards))
            value = self.total(cards)
            print(value)
            cards.append(value)
            return cards
            
            

    def erase_value_in_card(self,card):
        c = str(card)
        if c.isdigit():
            return False
        return True

    def total(self,cards):
        t = 0
        for card in cards:
            t = card[1] + t   
        return t
    # c = list(filter(lambda v: v[1] != self.value, cards))
        # if len(c) == 0:
        #     for card in cards:
        #         self.cards.append(card)
        #     return True

        # newCardsTotal = self.total(cards)
        # if newCardsTotal == self.value:
        #     for card in cards:
        #         self.cards.append(card)
        #     return True

        # return False     
    
    

            