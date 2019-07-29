# from src.controller.blackjackController import BlackjackController
#
#
# def main():
#     new_game = BlackjackController()
#     new_game.get_players_hand()
#
#     player_score = new_game.hit_player()
#     print(player_score)
#
#     # print('Players hand')
#     #
#     # print('Dealers hand')
#     # print(d)
#
#
# main()
from src.view.viewHandler import BlackjackMain

def main():
    BlackjackMain().mainloop()
    # dir = os.getcwd()

main()