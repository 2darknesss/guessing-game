import random

class Number:
    def __init__(self):
        self.value = random.randint(1, 99)

    def is_even(self):
        return self.value % 2 == 0

    def is_match(self, guess):
        return str(self.value) == guess

class User:
    def __init__(self):
        self.score = 10

    def decrease_score(self):
        self.score -= 1

class Game:
    def __init__(self):
        self.number = Number()
        self.user = User()

    def run(self):
        print("The game is started")
        while True:
            users_number = input("Guess the number: ")
            if users_number == 'exit':
                break
            elif users_number == 'is the number even':
                if self.number.is_even():
                    print('The number is even')
                else:
                    print("the number is odd ")
            elif self.number.is_match(users_number):
                print("You won")
                print(f'Your score {self.user.score}')
                break
            else:
                print("You lose")
            self.user.decrease_score()

if __name__ == "__main__":
    game = Game()
    game.run()
