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
        self.player1_deck_of_card, self.player2_deck_of_card = self.Game.players_deck_of_card()
        self.playerOne = Player("Jimmy", self.player1_deck_of_card)
        self.playerTwo = Player('Peter', self.player2_deck_of_card)
    def run(self):
        while True:
            if self.no_more_cards():
                break
            else:
                if self.playerOne.deck_of_cards:
                    self.next_play(self.playerOne)
                    os.system(var)
                else:
                    pass
                if self.playerTwo.deck_of_cards:
                    self.next_play(self.playerTwo)
                    os.system(var)
                else:
                    pass
                break
            
        # os.system(var)
        # self.Game.check_winner(self.playerOne,self.playerTwo)
        

    # make player moves
    def next_play(self,player):
        while True:
            print('Mesa de Juego',self.table)
            print(player.name,list(enumerate(player.deck_of_cards)))
            print('Digite 1 para Descartar Carta, ', 'Digite 2 para Tomar Carta, ', 'Digite 3 para realizar una construcción','Digite 4 para duplicar Carta, ', 'Digite 5 para incrementar una contruccion, ')
            user = int(input('Digite la jugada que quiera realizar : '))

            if user == 1: ## Descartar carta
                print('Digite 0 si desea cambiar la jugada, ','Digite 1 si desea continuar')
                user_action = int(input('Que acción tomara? : '))
                if user_action == 1:
                    print(player.name,list(enumerate(player.deck_of_cards)))
                    user_action = int(input('Que carta desea descartar?? : '))
                    self.table.append(player.deck_of_cards[user_action])
                    del player.deck_of_cards[user_action]
                    print(player.deck_of_cards,self.table)
                    break
                else:
                    pass

            elif user == 2: #Tomar carta
                
                    print('Digite 0 si desea cambiar la jugada, ','Digite 1 si desea continuar a tomar una carta')
                    user_action = int(input('Que acción tomara? : '))
                    if user_action == 1:
                        print('Mesa de Juego',list(enumerate(self.table)))
                        print(player.name,list(enumerate(player.deck_of_cards)))
                        print('Digite 0 si desea cambiar la jugada, ','Digite 1 si tiene cartas para realizar esta accion')
                        if user_action == 1:
                            while True: 
                                user_action = int(input('Que carta desea tomar de la mesa? : '))
                                user_actionTwo = int(input('Cual carta usted desea utilizar? : '))
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
                        else:
                            pass         
                    else:
                        pass
    
            elif user == 3: #Building a constructor card
                print('Digite 0 si desea cambiar la jugada, ','Digite 1 si desea continuar')
                user_action = int(input('Que acción tomara? : '))
                if user_action == 1:
                    print('Mesa de Juego',list(enumerate(self.table)))
                    print(player.name,list(enumerate(player.deck_of_cards)))
                    user_action = int(input('Que carta desea duplicar de la mesa(El valor de la duplicacion no puede valer más de 10)? : '))
                    user_actionTwo = int(input('Cual carta usted desea utilizar? : '))
                else:
                    break
                
           

        # check cards from table to be grabbed
        # player.deck_of_cards_grabbed = cards to grab
        # remove matching cards from table

    def no_more_cards(self):
        return len(self.deck.cards) == 0 and len(self.player1.deck_of_cards) == 0 and len(self.player2.deck_of_cards) == 0




play = Play()
play.run()



        