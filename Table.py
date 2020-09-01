class Table: 
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)

    # TODO: Remove cards from table
    def remove_cards(self,card_in_table):
        self.cards_in_table = card_in_table
        del self.cards[self.cards_in_table]
    def __str__(self):
        count = 0
        for card in self.cards:
            print(count,card)
            count = count + 1 
        return 'Game Table'