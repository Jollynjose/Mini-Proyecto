from Card import *
from constant import*

print('Casino, Juego de cartas')
print('Reglas:')
print('1 - las cartas se cuenta desde 0 no desde 1 ( el conteo sería: carta 1(0), carta 2(1), etc-')
count = 0
# while True:
#     if count < 2 :
#         ##Shift System
#         properties.turn()
#         if properties.playerturn == 0: 
#             player= player1.name
#             player_mazo = player1.mazo
#             player_deck_points= player1.deck
#         else:
#             player= player2.name
#             player_mazo = player2.mazo
#             player_deck_points= player2.deck
#         #Start Game
#         print('Digite la acción que quiera realizar en este juego : ')
#         print('Digite 1 para Descartar Carta, ', 'Digite 2 para Tomar Carta, ', 'Digite 3 para duplicar Carta, ', 'Digite 4 para incrementar una contruccion, ')
#         print('Mesa del Juego ', list(enumerate(properties.table)))
#         print('Su Mazo',list(enumerate(player_mazo)))
#         user = int(input())
#         if user == 1:
#             print('Cual carta desea descartar?')
#             select = int(input())
#             properties.table.append(player_mazo[select])
#             del player_mazo[select]
#         elif user == 2:
#             print('Cual carta desea tomar?')
#             for x in range(len(properties.table)):
#                 select = int(input())
#                 select2 = int(input())
#                 if int(player_mazo[select][1]) == int(properties.table[select2][1]):
#                     player_deck_points.append(player_mazo[select])
#                     player_deck_points.append(properties.table[select2])
#                     del player_mazo[select]
#                     del properties.table[select2]
#                     break
#                 else:
#                     print('La carta que usted quiere tomar no son compatibles, por favor seleccione bien su carta')


#         # for cards_in_player in range(len(player_mazo)):
#         #     for cards_on_table in range(len(properties.table)):
#         #         if int(player_mazo[cards_in_player][1]) == int(properties.table[cards_on_table][1]):
#         #             player_deck_points.append(player_mazo[cards_in_player])
#         #             player_deck_points.append(properties.table[cards_on_table])
#         #             del player_mazo[cards_in_player]
#         #             del properties.table[cards_on_table]
#         #             break
#         #         else:
#         #             properties.table.append(player_mazo[cards_in_player])
#         #             del player_mazo[cards_in_player]
#         #             break
#         #     break
#         count = count + 1
#     else:
#         break

                
                    
print(player1.mazo,player2.mazo,properties.table)










