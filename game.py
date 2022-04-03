from ai import AI
from human import Human
import random
from getpass import getpass
from time import sleep

class Game:
    def __init__(self):
        pass
            
    def start_game():
        player_one = Human("Player One")
        player_two = Human("Player Two")
        ai = AI("Hal")
        print('''

Welcome to Rock, Paper, Scissors, Lizard, Spock!

The best of two out of three games wins.

Choose your gesture by entering the associated number.

Use the number keys to choose 1P vs 2P or 1P vs AI

Here are the available gestures and their abilities.

*********************************************************************''')
        
        sleep(5)
        
        print('''

Rock crushes Scissors and Lizard.

Paper covers Rock and disproves Spock.

Scissors cut Paper and decapitate Lizard.

Lizard poisons Spock and eats Paper.

Spock smashes Scissors and vaporizes Rock.

*********************************************************************''')

        sleep(5)

        print('''

Which game mode would you like to choose?

Press 1 for 1P vs AI
Press 2 for 1P vs 2P
        ''')
         
        def choose_game_mode():
            game_mode = " "
          
            while True:
                game_mode = int(input("Game mode: "))
                print('''
*********************************************************************''')

                if game_mode == 1:
                    player_vs_ai_battle()
                    break

                elif game_mode == 2:
                    player_vs_player_battle()
                    break
                
                else:
                    print("")
                    print("Please choose either \"1\" or \"2\"")
                    choose_game_mode()

        def new_game_1p_vs_ai():
                new_game = input("Would you like to play again? Type Yes or No. ")

                if new_game == "No":
                        quit()

                elif new_game == "Yes":
                        player_one.wins = 0
                        ai.wins = 0
                        player_vs_ai_battle()

                else:
                    print("")
                    print("Please enter either Yes or No.")
                    new_game_1p_vs_ai()

        def new_game_1p_vs_2p():
                print("")
                new_game = input("Would you like to play again? Type Yes or No. ")

                if new_game == "No":
                        quit()

                elif new_game == "Yes":
                        player_one.wins = 0
                        player_two.wins = 0
                        ai.wins = 0
                        player_vs_player_battle()

                else:
                    print("")
                    print("Please enter either Yes or No.")
                    new_game_1p_vs_2p()
                    
        def player_vs_ai_battle():
                
                if player_one.wins == 2:
                    sleep(2)
                    print("")
                    print("*********************************************************************")
                    print("")
                    print(f"{player_one.name} won the game!")
                    new_game_1p_vs_ai()
                  
                elif ai.wins == 2:
                    sleep(2)
                    print("")
                    print("*********************************************************************")
                    print("")
                    print(f"{ai.name} won the game!")
                    new_game_1p_vs_ai()

                print('''

Choose your gesture!

0 = Rock
1 = Paper
2 = Scissors
3 = Lizard
4 = Spock        

*********************************************************************''')

                print("")

                chosen_gesture = int(input("Player One chosen gesture: "))

                while chosen_gesture not in [0,1,2,3,4]:
                    print("")
                    print("Please enter a number between 0 and 4.")
                    chosen_gesture = " "
                    player_vs_ai_battle()

                player_one.chosen_gesture = player_one.gestures[chosen_gesture]

                ai.chosen_gesture = ai.gestures[random.randint(0,4)]

                print("f{player_one.name} chose {player_one.chosen_gesture} and {ai.name} chose {ai.chosen_gesture}.")

                print("")

                if player_one.chosen_gesture == ai.chosen_gesture:
                    sleep(1.5)
                    print("It's a tie!")
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Rock" and (ai.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Paper" and (ai.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    sleep(1.5)
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Scissors" and (ai.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Lizard" and (ai.chosen_gesture == "Spock" or ai.chosen_gesture == "Paper"):
                    sleep(1.5)
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Spock" and (ai.chosen_gesture == "Scissors" or ai.chosen_gesture == "Rock"):
                    sleep(1.5)
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Rock" and (ai.chosen_gesture == "Paper" or ai.chosen_gesture == "Spock"):
                    sleep(1.5)
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle()    

                elif player_one.chosen_gesture == "Paper" and (ai.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Scissors" and (ai.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    sleep(1.5)
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Lizard" and (ai.chosen_gesture == "Rock" or ai.chosen_gesture == "Scissors"):
                    sleep(1.5)
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Spock" and (ai.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle()

        def player_vs_player_battle():
                
                if player_one.wins == 2:
                    sleep(2)
                    print("")
                    print("*********************************************************************")
                    print("")
                    print(f"{player_one.name} won the game!")
                    new_game_1p_vs_2p()

                elif player_two.wins == 2:
                    sleep(2)
                    print("")
                    print("*********************************************************************")
                    print("")
                    print(f"{player_two.name} won the game!")
                    new_game_1p_vs_2p()
                print('''

Choose your gesture!

0 = Rock
1 = Paper
2 = Scissors
3 = Lizard
4 = Spock        

*********************************************************************''')

                print("")

                player_one_chosen_gesture = int(getpass("Player One chosen gesture: "))

                while player_one_chosen_gesture not in [0, 1, 2, 3, 4]:
                    print("")
                    print("Please enter a number between 0 and 4.")
                    player_one_chosen_gesture = " "
                    player_vs_player_battle()

                player_one.chosen_gesture = player_one.gestures[player_one_chosen_gesture]

                print("")

                player_two_chosen_gesture = int(getpass("Player Two chosen gesture: "))

                while player_two_chosen_gesture not in [0, 1, 2, 3, 4]:
                    print("")
                    print("Please enter a number between 0 and 4.")
                    player_two_chosen_gesture = " "
                    player_vs_player_battle()

                player_two.chosen_gesture = player_two.gestures[player_two_chosen_gesture]

                print(f'''
{player_one.name} chose {player_one.chosen_gesture} and {player_two.name} chose {player_two.chosen_gesture}.
                ''')

                if player_one.chosen_gesture == player_two.chosen_gesture:
                    sleep(1.5)
                    print("It's a tie!")
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Rock" and (player_two.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Paper" and (player_two.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    sleep(1.5)
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Scissors" and (player_two.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Lizard" and (player_two.chosen_gesture == "Spock" or ai.chosen_gesture == "Paper"):
                    sleep(1.5)
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Spock" and (player_two.chosen_gesture == "Scissors" or ai.chosen_gesture == "Rock"):
                    sleep(1.5)
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Rock" and (player_two.chosen_gesture == "Paper" or ai.chosen_gesture == "Spock"):
                    sleep(1.5)
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()
                    
                elif player_one.chosen_gesture == "Paper" and (player_two.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Scissors" and (player_two.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    sleep(1.5)
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Lizard" and (player_two.chosen_gesture == "Rock" or ai.chosen_gesture == "Scissors"):
                    sleep(1.5)
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Spock" and (player_two.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    sleep(1.5)
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

        choose_game_mode()