class Computer:

    answers = {
        # Possible user answers categorized
        "y_n": {
            "yes": True,
            "y": True,
            "ye": True,
            "no": False,
            "n": False
        },
        "h_l": {
            "high": True,
            "higher": True,
            "h": True,
            "low": False,
            "lower": False,
            "l": False
        }
    }

    def __init__(self):
        self.comp_range = [None, None]
        self.player_num = None

    def set_range(self, give_range=None):
        if give_range is None:
            y_n = input("Would you like to set a range for me to guess in? ")
            try:
                user_answer = self.answers["y_n"][y_n]
            except KeyError:
                print("Invalid answer. Try again.")
                self.set_range()
            else:
                if user_answer:
                    self.set_min()
                    self.set_max()
                else:
                    self.set_range([1, 100])
        else:
            self.comp_range = give_range

    def set_min(self, give_min=None):
        if give_min is None:
            try:
                range_min = int(input("Give me a minimum number: "))
            except ValueError:
                print("Invalid answer. Try again.")
                self.set_min()
            else:
                self.comp_range[0] = range_min
        else:
            self.comp_range = [give_min, self.comp_range[1]]

    def set_max(self, give_max=None):
        if give_max is None:
            try:
                range_max = int(input("Give me a maximum number: "))
            except ValueError:
                print("Invalid answer. Try again.")
                self.set_max()
            else:
                if range_max > self.comp_range[0] + 1:
                    self.comp_range[1] = range_max
                else:
                    print("Invalid range. Try again.")
                    self.set_max()
        else:
            self.comp_range = [self.comp_range[0], give_max]

    def guess(self):
        comp_guess = (self.comp_range[0] + self.comp_range[1]) // 2
        y_n = input(f"Is your number {comp_guess}? y/n? ").lower()
        try:
            user_answer = self.answers["y_n"][y_n]
        except KeyError:
            print("Invalid answer. Try again.")
            return self.guess()
        else:
            if user_answer:
                self.player_num = comp_guess
                return True
            else:
                self.high_low(comp_guess)

    def high_low(self, comp_guess):
        h_l = input(f"Is your number higher or lower than {comp_guess}? ").lower()
        try:
            user_answer = self.answers["h_l"][h_l]
        except KeyError:
            print("Invalid answer. Try again.")
            self.high_low(comp_guess)
        else:
            if user_answer:
                self.set_min(comp_guess)
            else:
                self.set_max(comp_guess)
            return False

    def think_of_a_number(self):
        input(f"Think of a number between {self.comp_range[0]} and {self.comp_range[1]}. Then press \"Enter\".")


def user_interface():
    print("Welcome to Number Guesser 1.0!")
    guess_bot_3000 = Computer()
    guess_bot_3000.set_range()
    guess_bot_3000.think_of_a_number()
    comp_guess = guess_bot_3000.guess()

    while not comp_guess:
        comp_guess = guess_bot_3000.guess()

    print(f"I have guessed your number correctly! It is {guess_bot_3000.player_num}.")
    print("Thank you for playing Number Guesser 1.0!")


user_interface()
