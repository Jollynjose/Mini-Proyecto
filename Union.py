class Union:
    def __init__(self,cards=[]):
        self.cards = cards
        self.value = self.total(self.cards)

    def add_cards(self,cards):
        c = list(filter(lambda v: v[1] != self.value, cards))
        if len(c) == 0:
            for card in cards:
                self.cards.append(card)
            return True

        newCardsTotal = self.total(cards)
        if newCardsTotal == self.value:
            for card in cards:
                self.cards.append(card)
            return True

        return False
            
    def total(self,cards):
        t = 0
        for card in cards:
            t += card[1]  
        return t
            