from Card import *
from Game import *
from Deck import *
from Player import *
from constants import *
from Union import *
import os
cls = lambda: os.system('cls')

class Play:
    def __init__(self):
        self.cards = Cards(Values, Suits)
        self.deck = Deck(self.cards.card())
        self.Game = Game_of_two(self.deck.initialize())
        self.Game.shuffle_cards()
        self.table = self.Game.create_table()
        self.check = []
        self.union = Union()
        self.cards_on_table = self.table.cards
        self.cards_union = self.table.unions_on_table
        self.playerOne = Player("Jimmy")
        self.playerTwo = Player('Peter')
       
    def run(self):
        while True:
            if self.no_more_cards():
                cls()
                print(self.Game.check_winner(self.playerOne,self.playerTwo))
                break
            else:
                if self.playerOne.deck_of_cards and self.playerTwo.deck_of_cards:
                    self.check= self.playerOne.deck_of_cards_grabbed
                    self.next_play(self.playerOne)
                    self.check= self.playerTwo.deck_of_cards_grabbed
                    self.next_play(self.playerTwo)
                else:
                    self.Game.players_deck_of_card(self.playerOne.deck_of_cards)
                    self.Game.players_deck_of_card(self.playerTwo.deck_of_cards)

    def check_duplicate(self):
        for x in range(len(self.cards_union)):
            if self.cards_union[x][1] == self.cards_union[x+1][1]:
                return False
            return True
           
    def checkunion(self,cards):
        for card in self.cards_union:
            if card == cards:
                return False
        return True

    def checktable(self,cards):
        for card in self.cards_on_table:
            if cards == card:
                return False
        return True
    
    def checkcard(self,cards):
        for card in self.check:
            if cards == card:
                return False
        return True

    def next_play(self,player):
        while True:
            try:
                if self.cards_on_table:    
                        print('Cassino The Card Game')
                        print('Game Table',self.cards_on_table)
                        print('Union',self.cards_union)
                        print(player.name,player.deck_of_cards)
                        print('Player cards grabbed', player.deck_of_cards_grabbed)
                        print('Introduce 1 if you want to discard a card, ','Introduce 2 if you want to take a card on table, ', 'Introduce 3 if you want to build a union')
                        user_action = int(input('what action would you take? : '))

                        if user_action == 1: ##discard card
                            print(list(enumerate(player.deck_of_cards)))
                            user_action = int(input('Which card would you discard? '))
                            cls()
                            self.cards_on_table.append((player.deck_of_cards[user_action]))
                            player.deck_of_cards = list(filter(self.checktable,player.deck_of_cards))
                            break     

                        elif user_action == 2: ##take card on table
                            cls()
                            print(list(enumerate(self.cards_on_table)))
                            print(player.name, list(enumerate(player.deck_of_cards)))
                            print('Introduce 1 if you want to take a one card,' ,'introduce 2 if you want to take Two cards on table, ', 'Introduce 3 if you want to take a Union')
                            user_action = int(input('Select your action : '))
                            if user_action == 1:
                                user_actionOne= int(input('Which card on the table would you take? : '))
                                user_actionTwo = int(input('Which card in your deck would you use? : '))
                                if self.cards_on_table[user_actionOne][1] == player.deck_of_cards[user_actionTwo][1]:
                                    player.deck_of_cards_grabbed.append(self.cards_on_table[user_actionOne])
                                    player.deck_of_cards_grabbed.append(player.deck_of_cards[user_actionTwo])
                                    self.cards_on_table = list(filter(self.checkcard,self.cards_on_table))
                                    player.deck_of_cards = list(filter(self.checkcard,player.deck_of_cards))
                                    break

                            elif user_action == 2:
                                user_actionOne= int(input('Which card on the table would you take? : '))
                                user_actionTwo = int(input('Which card on the table would you take? : '))
                                user_actionThree = int(input('Which card in your deck would you use? : '))
                                if self.cards_on_table[user_actionOne][1] + self.cards_on_table[user_actionTwo][1] <= 10 :
                                    if self.cards_on_table[user_actionOne][1] + self.cards_on_table[user_actionTwo][1] == player.deck_of_cards[user_actionThree][1]:
                                        player.deck_of_cards_grabbed.append(self.cards_on_table[user_actionOne])
                                        player.deck_of_cards_grabbed.append(self.cards_on_table[user_actionTwo])
                                        player.deck_of_cards_grabbed.append(player.deck_of_cards[user_actionThree])
                                        self.cards_on_table = list(filter(self.checkcard,self.cards_on_table))
                                        player.deck_of_cards = list(filter(self.checkcard, player.deck_of_cards))
                                        break

                                    else:
                                        cls()
                                        print('Wrong card')

                                else: 
                                    cls()
                                    print('Wrong play')

                            elif user_action == 3:
                                if self.cards_union:
                                    print(self.union_table)
                                    print(list(enumerate(player.deck_of_cards)))
                                    user_actionOne = int(input('Which card in your deck would you use? : '))
                                    if player.deck_of_cards[user_actionOne] == self.cards_union[-1]:
                                        self.cards_union.pop()
                                        for x in self.cards_union:
                                            player.deck_of_cards_grabbed.append(x)
                                        self.cards_union = list(filter(lambda v : False ,self.cards_union))
                                    else: 
                                        cls()
                                        print( 'Wrong play')
                                else:
                                    cls()
                                    print('there are not cards in union')
                            
                        elif user_action == 3:
                            print('Introduce 1 if you want to create a union, ', 'Introduce 2 if you want to increase a union ')
                            user_action = int(input(''))
                            if user_action == 1:
                                if  self.cards_union:
                                    print('The game has not supported more unions')
                                else:
                                    cls()
                                    print(list(enumerate(self.cards_on_table)))
                                    print(list(enumerate(player.deck_of_cards)))
                                    user_actionOne = int(input('How card on the table you want to make a union? : '))
                                    user_actionTwo = int(input('How card do you use in your deck cards? : '))
                                    if self.cards_on_table[user_actionOne] + player.deck_of_cards[user_actionTwo] >= 13:
                                        if self.cards_on_table[user_actionOne] == player.deck_of_cards[user_actionTwo]:
                                            self.cards_union.append(self.cards_on_table.pop(user_actionOne))
                                            self.cards_union.append(player.deck_of_cards.pop(user_actionTwo))
                                            self.cards_union = self.union.add_card(self.cards_union)
                                            break
                                        else:
                                            print('The value of the union must be less than 13')
                                    else:
                                        self.cards_union.append(self.cards_on_table.pop(user_actionOne))
                                        self.cards_union.append(player.deck_of_cards.pop(user_actionTwo))
                                        self.cards_union = self.union.add_card(self.cards_union)
                                        break
                                    

                            elif user_action == 2:
                                if self.cards_union:
                                    if self.cards_union[-1] <= 10:
                                        print('How much do you want incremate?')
                                        print(self.cards_union)
                                        print(list(enumerate(player.deck_of_cards)))
                                        user_actionOne = int(input(''))
                                        if self.cards_union[0][1] == self.cards_union[1][1]:
                                            cls()
                                            print('it is a duplicate union, Repeat the play')
                                        else:
                                            if player.deck_of_cards[user_actionOne] + self.cards_union[-1] < 14:
                                                cls()
                                                self.cards_union.append(player.deck_of_cards.pop(user_actionOne))
                                                self.cards_union = self.union.add_card(self.cards_union)
                                                break
                                            else:
                                                cls()
                                                print('the increase does not comply with the rules, Do other action ')
                                else:
                                    cls()
                                    print('There are not cards in union')
                    
                            

                        else:
                            print(list(enumerate(player.deck_of_cards)))
                            user_action = int(input('Which card would you discard? '))
                            self.cards_on_table.append((player.deck_of_cards[user_action]))
                            player.deck_of_cards = list(filter(self.checktable,player.deck_of_cards))
                            break
            except:
                cls()
                print('ONLY INTEGERS')


    def no_more_cards(self):
        return len(self.deck.cards) == 0 and len(self.player1.deck_of_cards) == 0 and len(self.player2.deck_of_cards) == 0

play = Play()
play.run()
