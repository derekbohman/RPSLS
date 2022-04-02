from ai import AI
from human import Human
import random

class Game:
    def __init__(self):
        pass
            
    def run_game():
        global game_mode
        game_mode = " "
        print('''
**************************************************

Welcome to Rock, Paper, Scissors, Lizard, Spock!

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

Which game mode would you like to choose?

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
                player_one = Human("Player One")
                player_two = AI("Player Two")
                
                if player_one.wins == 2:
                    print("You win!")

                elif player_two.wins == 2:
                    print("You lose.")

                print('''
Here are your gesture options.

Rock
Paper
Scissors
Lizard
Spock        
                ''')
                player_one.chosen_gesture = input("Choose a gesture: ")
                player_two.chosen_gesture = random.choice(player_two.gestures)

                print(f'''
{player_one.name} chose {player_one.chosen_gesture} and 

{player_two.name} chose {player_two.chosen_gesture}
                ''')

                if player_one.chosen_gesture == player_two.chosen_gesture:
                    print("It's a tie!")
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Rock" and player_two.chosen_gesture == "Scissors" or "Lizard":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Paper" and player_two.chosen_gesture == "Rock" or "Spock":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Scissors" and player_two.chosen_gesture == "Paper" or "Lizard":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Lizard" and player_two.chosen_gesture == "Spock" or "Paper":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Spock" and player_two.chosen_gesture == "Scissors" or "Rock":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Rock" and player_two.chosen_gesture == "Paper" or "Spock":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_ai_battle()     

                elif player_one.chosen_gesture == "Paper" and player_two.chosen_gesture == "Scissors" or "Lizard":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Scissors" and player_two.chosen_gesture == "Rock" or "Spock":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Lizard" and player_two.chosen_gesture == "Rock" or "Scissors":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Spock" and player_two.chosen_gesture == "Paper" or "Lizard":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_ai_battle

        def player_vs_player_battle():
                player_one = Human("Player One")
                player_two = Human("Player Two")
                
                if player_one.wins == 2:
                    print("Player One Wins!")

                elif player_two.wins == 2:
                    print("Player Two Wins!")

                print('''
Here are your gesture options.

Rock
Paper
Scissors
Lizard
Spock        
                ''')
                player_one.chosen_gesture = input("Choose a gesture: ")
                player_two.chosen_gesture = input("Choose a gesture: ")

                print(f'''
{player_one.name} chose {player_one.chosen_gesture} and 

{player_two.name} chose {player_two.chosen_gesture}
                ''')

                if player_one.chosen_gesture == player_two.chosen_gesture:
                    print("It's a tie!")
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Rock" and player_two.chosen_gesture == "Scissors" or "Lizard":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Paper" and player_two.chosen_gesture == "Rock" or "Spock":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Scissors" and player_two.chosen_gesture == "Paper" or "Lizard":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Lizard" and player_two.chosen_gesture == "Spock" or "Paper":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Spock" and player_two.chosen_gesture == "Scissors" or "Rock":
                    print("You win!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Rock" and player_two.chosen_gesture == "Paper" or "Spock":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_player_battle()()
                    
                elif player_one.chosen_gesture == "Paper" and player_two.chosen_gesture == "Scissors" or "Lizard":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Scissors" and player_two.chosen_gesture == "Rock" or "Spock":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Lizard" and player_two.chosen_gesture == "Rock" or "Scissors":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Spock" and player_two.chosen_gesture == "Paper" or "Lizard":
                    print("You lose!")
                    player_two.wins += 1
                    player_vs_player_battle()