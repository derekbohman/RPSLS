import random

class Player:
    def __init__(self, name):
        self.name = name
        self.chosen_gesture = " "
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.wins = 0

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)