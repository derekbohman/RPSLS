from player import Player


class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = "AI"