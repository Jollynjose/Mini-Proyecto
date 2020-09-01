class Cards:
    def __init__(self, Values, Suits): # Lo que tiene una carta
        self.Values = Values
        self.Suits = Suits
        
    # TODO: change name 
    def card(self):
        cards = self.Suits, self.Values
        return cards
