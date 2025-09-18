import random


class Die:

    def __init__(self):
        self._die = None

    # MethodsGa
    def roll(self):
        """Get a value to the die between 1-6 inclusive"""
        self._die = random.randint(1, 6)

    @property
    def die_value(self):
        """Getter to obtain the value of the non-public die attribute"""
        return self._die


class Player:

    def __init__(self, die, is_human=True):
        self.die = die  # aggregation
        self.is_human = is_human
        self.counter = 10

    # Methods
    def increment(self):
        """Increment by one, the value of the counter"""
        self.counter += 1

    def decrement(self):
        """Decrement by one, the value of the counter"""
        self.counter -= 1

    def roll_die(self):
        """Simulate the rolling of a die"""
        self.die.roll()
        return self.die.die_value


class DiceGame:

    def __init__(self):
        self.human_player = Player(Die(), is_human=True)  # aggregation
        self.computer_player = Player(Die(), is_human=False)  # aggregation

    # Methods
    def start_game(self):
        print("""Welcome to the Dice Game""")
        while self.human_player.counter > 0 and self.computer_player.counter > 0:
            self.start_round()

        if self.human_player.counter == 0:
            print("\nHuman player wins the game!")
        else:
            print("\nComputer player wins the game!")

    def start_round(self):
        print('The round is already started!')
        start_key = input('Press any key to start the game and roll your die!')

        if isinstance(start_key, str):
            human_value_die = self.human_player.roll_die()
            computer_value_die = self.computer_player.roll_die()

            print(f"Your die value is: {human_value_die}")
            print('The computer is rolling its die...')
            print(f"Computer die value: {computer_value_die}")

            if human_value_die > computer_value_die:
                self.human_player.decrement()
                self.computer_player.increment()
                print('\nYou win this match!\nCONGRATULATIONS!!!')
                print(f'Current counter:\n{self.human_player.counter}\n{self.computer_player.counter}')
            elif computer_value_die > human_value_die:
                self.computer_player.decrement()
                self.human_player.increment()
                print('\nThe computer win this match!')
                print(f'Current counter:\n{self.human_player.counter}\n{self.computer_player.counter}')
            else:
                print('\nNobody win this match')
                print(f'Current counter:\n{self.human_player.counter}\n{self.computer_player.counter}')
        else:
            print('Please enter a valid key')


# Complete game
game = DiceGame()
game.start_game()
