from ai import AI
from human import Human
from player import Player
import random

class Game:
    def __init__(self):
        self.player_1 = Human()
        self.player_2 = Human()
        self.ai = AI()
            
    def run_game():
        global game_mode
        game_mode = " "
        print('''
**************************************************

Welcome to Rock, Paper, Scissors, Lizard, Spock!
        ''')
        user_name = input("What is your name? ")
        print(f'''
The winner is the best of two out of three games.

Use the number keys to choose your gesture.

Use the number keys to choose 1P vs 2P or 1P vs AI

Here are the available gestures and their actions.

Rock crushes Scissors
Rock crushes Lizard
Paper covers Rock
Paper disproves Spock
Scissors cut Paper
Scissors decapitate Lizard
Lizard poisons Spock
Lizard eats Paper
Spock smashes Scissors
Spock vaporizes Rock

**************************************************

Which game mode would you like to choose {user_name}?

Press 1 for 1P vs 2P
Press 2 for 1P vs AI
         ''')

        def choose_game_mode():
           
            while True:
                game_mode = int(input("Game mode: "))
               
                if game_mode == 1:
                    player_vs_ai_battle()
                    break

                if game_mode == 2:
                    player_vs_player_battle()
                    break
                
                print("")
                print("Please choose either \"1\" or \"2\"")
                print("")
                choose_game_mode()

        def player_vs_ai_battle():
            