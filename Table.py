
class Table: 
    def __init__(self):
        self.cards = []
        
        self.unions_on_table = [] # [Union [3, 3, 1, 2] value 3, Union [6, 6, 3, 3] value 6]
        # self.cards_on_table = []  # [1, 5]
        
    def add_card(self, card):
        self.cards.append(card)
        return self.cards
        
    def __str__(self):
        count = 0
        for card in self.cards:
            print(count,card)
            count = count + 1 
        return 'Game Table'
    
    
