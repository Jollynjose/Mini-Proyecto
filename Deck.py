class Deck:
    # TODO: set special cards

    def __init__(self, cards):
        self.cards = cards
    def initialize(self): #todas las cartas que lleva un deck
        suits , values = self.cards
        deck = []
        for suit in suits:
            for value in values:
                deck.append([suit,value])
        return deck
