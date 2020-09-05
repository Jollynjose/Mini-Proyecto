class Table: 
    def __init__(self):
        self.cards = []
        self.cards_on_table = []
    def add_card(self, card):
        self.cards.append(card)
        
    def __str__(self):
        count = 0
        for card in self.cards:
            print(count,card)
            count = count + 1 
        return 'Game Table'