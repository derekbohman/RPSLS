from ai import AI
from human import Human
import random
from getpass import getpass

class Game:
    def __init__(self):
        pass
            
    def start_game():
        player_one = Human("Player One")
        player_two = Human("Player Two")
        ai = AI("Hal")
        global game_mode
        game_mode = " "
        print('''
**************************************************

Welcome to Rock, Paper, Scissors, Lizard, Spock!

The winner is the best of two out of three games.

Please type in your gesture as it appears in the list.

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

Press 1 for 1P vs AI
Press 2 for 1P vs 2P
         ''')
        def choose_game_mode():
          
            while True:
                game_mode = int(input("Game mode: "))
               
                if game_mode == 1:
                    player_vs_ai_battle()
                    break

                elif game_mode == 2:
                    player_vs_player_battle()
                    break
                
                else:
                    print("")
                    print("Please choose either \"1\" or \"2\"")
                    print("")
                    choose_game_mode()

        def player_vs_ai_battle():
                
                if player_one.wins == 2:
                    print("")
                    print(f"{player_one.name} won the game!")
                    quit()

                elif ai.wins == 2:
                    print("")
                    print(f"{ai.name} won the game!")
                    quit()

                print('''
Here are your gesture options.

Rock
Paper
Scissors
Lizard
Spock        
                ''')
                player_one.chosen_gesture = input("Choose a gesture: ")
                ai.chosen_gesture = random.choice(ai.gestures)

                print(f'''
{player_one.name} chose {player_one.chosen_gesture} and 

{ai.name} chose {ai.chosen_gesture}
                ''')

                if player_one.chosen_gesture == ai.chosen_gesture:
                    print("It's a tie!")
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Rock" and (ai.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle()

                elif player_one.chosen_gesture == "Paper" and (ai.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Scissors" and (ai.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Lizard" and (ai.chosen_gesture == "Spock" or ai.chosen_gesture == "Paper"):
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Spock" and (ai.chosen_gesture == "Scissors" or ai.chosen_gesture == "Rock"):
                    print("You win!")
                    player_one.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Rock" and (ai.chosen_gesture == "Paper" or ai.chosen_gesture == "Spock"):
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle()    

                elif player_one.chosen_gesture == "Paper" and (ai.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Scissors" and (ai.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Lizard" and (ai.chosen_gesture == "Rock" or ai.chosen_gesture == "Scissors"):
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle

                elif player_one.chosen_gesture == "Spock" and (ai.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    print("You lose!")
                    ai.wins += 1
                    player_vs_ai_battle

        def player_vs_player_battle():
                
                if player_one.wins == 2:
                    print("")
                    print(f"{player_one.name} won the game!")
                    quit()

                elif player_two.wins == 2:
                    print("")
                    print(f"{player_two.name} won the game!")
                    quit()

                print('''
Here are your gesture options.

Rock
Paper
Scissors
Lizard
Spock        
                ''')
                player_one.chosen_gesture = getpass("Player One, choose a gesture: ")
                player_two.chosen_gesture = getpass("Player Two, choose a gesture: ")

                print(f'''
{player_one.name} chose {player_one.chosen_gesture} and 

{player_two.name} chose {player_two.chosen_gesture}
                ''')

                if player_one.chosen_gesture == player_two.chosen_gesture:
                    print("It's a tie!")
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Rock" and (player_two.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Paper" and (player_two.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Scissors" and (player_two.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Lizard" and (player_two.chosen_gesture == "Spock" or ai.chosen_gesture == "Paper"):
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Spock" and (player_two.chosen_gesture == "Scissors" or ai.chosen_gesture == "Rock"):
                    print(f"{player_one.name} wins!")
                    player_one.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Rock" and (player_two.chosen_gesture == "Paper" or ai.chosen_gesture == "Spock"):
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()
                    
                elif player_one.chosen_gesture == "Paper" and (player_two.chosen_gesture == "Scissors" or ai.chosen_gesture == "Lizard"):
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Scissors" and (player_two.chosen_gesture == "Rock" or ai.chosen_gesture == "Spock"):
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Lizard" and (player_two.chosen_gesture == "Rock" or ai.chosen_gesture == "Scissors"):
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

                elif player_one.chosen_gesture == "Spock" and (player_two.chosen_gesture == "Paper" or ai.chosen_gesture == "Lizard"):
                    print(f"{player_two.name} wins!")
                    player_two.wins += 1
                    player_vs_player_battle()

        choose_game_mode()