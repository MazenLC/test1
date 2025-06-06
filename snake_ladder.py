import random

# Board configuration for snakes and ladders
SNAKES = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78,
}

LADDERS = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100,
}


class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 0

    def move(self, steps: int):
        if self.position + steps <= 100:
            self.position += steps

        # Check for snakes or ladders
        self.position = SNAKES.get(self.position, self.position)
        self.position = LADDERS.get(self.position, self.position)

        return self.position


class Game:
    def __init__(self, players):
        self.players = players
        self.current = 0
        self.winner = None

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self):
        player = self.players[self.current]
        roll = self.roll_dice()
        new_pos = player.move(roll)
        print(f"{player.name} rolled a {roll} and moved to {new_pos}")

        if new_pos == 100:
            self.winner = player
        else:
            self.current = (self.current + 1) % len(self.players)

    def start(self):
        print("Starting Snakes and Ladders! First to reach 100 wins.")
        while not self.winner:
            input(f"{self.players[self.current].name}'s turn. Press Enter to roll the dice...")
            self.play_turn()
        print(f"{self.winner.name} wins!")


def main():
    p1_name = input("Enter name for Player 1: ") or "Player 1"
    p2_name = input("Enter name for Player 2: ") or "Player 2"

    game = Game([Player(p1_name), Player(p2_name)])
    game.start()


if __name__ == "__main__":
    main()
