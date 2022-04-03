from player import Player


class AI(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        return super().choose_gesture()