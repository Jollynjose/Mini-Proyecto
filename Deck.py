class Deck:
    # TODO: set special cards

    def __init__(self, cards):
        self.cards = cards
    def initialize(self): #All cards in deck
        suits , values = self.cards
        deck = []
        for suit in suits:
            for value in values:
                deck.append([suit,value])
        return deck
