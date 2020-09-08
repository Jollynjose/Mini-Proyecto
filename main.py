from Card import *
from Game import *
from Deck import *
from Player import *
from constants import *


class Play:
    def __init__(self):
        self.cards = Cards(Values, Suits)
        self.deck = Deck(self.cards.card())
        self.Game = Game_of_two(self.deck.initialize())
        self.Game.shuffle_cards()
        self.table = self.Game.create_table()
        self.cards_on_table = self.table.cards
        self.player1_deck_of_card, self.player2_deck_of_card = self.Game.players_deck_of_card()
        self.playerOne = Player("Jimmy", self.player1_deck_of_card)
        self.playerTwo = Player('Peter', self.player2_deck_of_card)
    def run(self):
        while True:
            
            if self.no_more_cards():
                #check winner
                break
            else:
                if self.playerOne.deck_of_cards and self.playerTwo.deck_of_cards:
                    self.next_play(self.playerOne)
                    self.next_play(self.playerTwo)
                    break
                                   
                else:
                    self.Game.players_deck_of_card()
    

    def next_play(self,player):
        while True:
            print('Cassino Card Game',player.deck_of_cards_grabbed)
            print('Game Table',list(enumerate(self.cards_on_table)))
            print(player.name,player.deck_of_cards)
            print('Introduce 1 if you want to discard a card, ','Introduce 2 if you want to take a card on table')
            user_action = int(input('what action would you take? : '))
            if user_action == 1: ##discard card
                print(list(enumerate(player.deck_of_cards)))
                user_action = int(input('Which card would you discard? '))
                self.discard_Card(player.deck_of_cards[user_action])
                player.deck_of_cards = list(filter(self.cards_on_table,player.deck_of_cards))
                break
            elif user_action == 2: ##take card on table
                print(list(enumerate(self.cards_on_table)))
                print(player.name, list(enumerate(player.deck_of_cards)))
                print('Introduce 1 if you want to take a one card, introduce 2 if you want to take Two cards on table')
                user_action = int(input(''))
                if user_action == 1:
                    user_actionOne= int(input('Which card on the table would you take? : '))
                    user_actionTwo = int(input('Which card in your deck would you use? : '))
                    if self.cards_on_table[user_actionOne][1] == player.deck_of_cards[user_actionTwo][1]:
                        player.deck_of_cards_grabbed.append(self.cards_on_table.pop(user_actionOne))
                        player.deck_of_cards_grabbed.append(player.deck_of_cards.pop(user_actionTwo))
                        self.cards_on_table = list(filter(None,self.cards_on_table))
                        player.deck_of_cards = list(filter(None, player.deck_of_cards))
                        break
                elif user_action == 2:
                    user_actionOne= int(input('Which card on the table would you take? : '))
                    user_actionTwo = int(input('Which card on the table would you take? : '))
                    user_actionThree = int(input('Which card in your deck would you use? : '))
                    if self.cards_on_table[user_actionOne][1] + self.cards_on_table[user_actionTwo][1] <= 10 :
                        if self.cards_on_table[user_actionOne][1] + self.cards_on_table[user_actionTwo][1] == player.deck_of_cards[user_actionThree][1]:
                            player.deck_of_cards_grabbed.append(self.cards_on_table.pop(user_actionOne))
                            player.deck_of_cards_grabbed.append(self.cards_on_table.pop(user_actionTwo))
                            player.deck_of_cards_grabbed.append(player.deck_of_cards.pop(user_actionThree))
                            self.cards_on_table = list(filter(None,self.cards_on_table))
                            player.deck_of_cards = list(filter(None, player.deck_of_cards))
                        else:
                            print('Wrong card')

                    else: 
                        print('Wrong play')


                


        

        
                
                
            
        # os.system(var)
        # self.Game.check_winner(self.playerOne,self.playerTwo)
        

    # make player moves
     

        # check cards from table to be grabbed
        # player.deck_of_cards_grabbed = cards to grab
        # remove matching cards from table

    def no_more_cards(self):
        return len(self.deck.cards) == 0 and len(self.player1.deck_of_cards) == 0 and len(self.player2.deck_of_cards) == 0

    def discard_Card(self,card):
        self.cards_on_table.append(card) 
        return self.cards_on_table

    def eliminate_cards_on_table(self,card):
        pass

play = Play()
play.run()



        