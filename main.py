from Card import *
from Game import *
from Deck import *
from Player import *
from constants import *
import os 

if os.name == "posix":
   var = "clear"        
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

class Play:
    def __init__(self):
        self.cards = Cards(Values, Suits)
        self.deck = Deck(self.cards.card())
        self.Game = Game_of_two(self.deck.initialize())
        self.Game.shuffle_cards()
        self.table = self.Game.create_table().cards
        self.card_on_table= self.Game.create_table().cards_on_table
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
                    os.system(var)
                    self.next_play(self.playerTwo)
                    os.system(var)                
                else:
                    self.Game.players_deck_of_card()

                
                
            
        # os.system(var)
        # self.Game.check_winner(self.playerOne,self.playerTwo)
        

    # make player moves
    def next_play(self,player):
        while True:
            print('Mesa de Juego',self.table)
            print('Cartas sobre la mesa',self.card_on_table)
            print(player.name,list(enumerate(player.deck_of_cards)))
            print('Digite 1 para Descartar Carta, ', 'Digite 2 para Tomar Carta, ', 'Digite 3 para realizar una construcción,','Digite 4 para duplicar Carta, ')
            user = int(input('Digite la jugada que quiera realizar : '))
            if user == 1: ## Descartar carta
                print('Digite 0 si desea cambiar la jugada, ','Digite 1 si quiere continuar')
                user_action = int(input('Que acción tomara? : '))
                if user_action == 1:
                    print(player.name,list(enumerate(player.deck_of_cards)))
                    user_action = int(input('Que carta desea descartar?? : '))
                    self.table.append(player.deck_of_cards[user_action])
                    del player.deck_of_cards[user_action]
                    break
                
                else:
                    pass

            elif user == 2: #Tomar carta
                    os.system(var)
                    print('Mesa de Juego',list(enumerate(self.table)))
                    print(player.name,list(enumerate(player.deck_of_cards)))
                    print('Digite 0 si desea cambiar la jugada, ','Digite 1 si tomar una carta individual en la mesa, ','digite 2 si quiere tomar 2 cartas, ','digite 3 si quiere tomar una construcción')
                    user_action = int(input('Que acción tomara? : '))
                    if user_action == 1:
                        while True: 
                            os.system(var)
                            print('Mesa de Juego',list(enumerate(self.table)))
                            print(player.name,list(enumerate(player.deck_of_cards)))
                            user_action = int(input('Que carta desea tomar de la mesa? : '))
                            user_actionTwo = int(input('Cual carta usted desea utilizar? : '))
                            if self.table[user_action][1] == player.deck_of_cards[user_actionTwo][1]:
                                player.deck_of_cards_grabbed.append(self.table[user_action])
                                player.deck_of_cards_grabbed.append(player.deck_of_cards[user_actionTwo])
                                del player.deck_of_cards[user_actionTwo]
                                del self.table[user_action]
                                print(player.deck_of_cards_grabbed,self.table)
                                break
                            else:
                                print('su carta que selecciono no es semejante, por favor considere su acción')
                        break
                    elif user_action == 2:
                        os.system(var)
                        print('Mesa del Juego',list(enumerate(self.table)))
                        print(player.name,list(enumerate(player.deck_of_cards)))
                        user_action = int(input('selecciona la carta que desea tomar : '))
                        user_actionTwo = int(input('seleccione la otra carta que desea tomar : '))
                        user_actionThree = int(input('seleccione la carta que desea utilizar : '))
                        if self.table[user_action][1]+ self.table[user_actionTwo][1] <= 10:
                            if self.table[user_action][1]+ self.table[user_actionTwo][1] == player.deck_of_cards[user_actionThree][1]:
                                player.deck_of_cards_grabbed.append(self.table[user_action])
                                player.deck_of_cards_grabbed.append(self.table[user_actionTwo])
                                player.deck_of_cards_grabbed.append(self.table[user_actionThree])
                                del self.table[user_action]
                                del self.table[user_actionTwo]
                                del player.deck_of_cards[user_actionThree]
                                break
                            else:
                                print('jugada no valida')
                        else:
                            print('No es permitido que el valor sea mayor que 10')
                    elif user_action == 3:
                        if self.card_on_table:
                            print(self.card_on_table)
                        else:
                            print('no hay construcciones')         
                    else:
                        pass
    
            elif user == 3: #Building a constructor card
                print('Digite 0 si desea cambiar la jugada, ','Digite 1 si desea realizar una construccion de cartas, Digite 2 si quiere incrementar la construcción')
                user_action = int(input('Que acción tomara? : '))
                if user_action == 1:
                    print(self.table)
                    user_action= int(input('que carta de la mesa quiere aumentar?'))
                    user_actionTwo= int(input)
                    pass
                elif user_action == 2:
                    if len(self.card_on_table):
                        pass
                    else:
                        print('No hay cartas para incrementar')
                        pass
                else:
                    break
                
           

        # check cards from table to be grabbed
        # player.deck_of_cards_grabbed = cards to grab
        # remove matching cards from table

    def no_more_cards(self):
        return len(self.deck.cards) == 0 and len(self.player1.deck_of_cards) == 0 and len(self.player2.deck_of_cards) == 0




play = Play()
play.run()



        