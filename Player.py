
class Player:
    def __init__(self, name):
        self.name = name
        self.deck_of_cards = []
        self.deck_of_cards_grabbed = [] #Search a better name
    def information(self):
        return self.name, self.deck_of_cards , len(self.deck_of_cards_grabbed)