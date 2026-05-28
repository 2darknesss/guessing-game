import random


def main():
    print("The game is started")

    num = random.randint(1,99)
    users_number = input("Guess the number: ")
    if num == users_number:
        print("You won")
    else: print("You lose")

    


if __name__ == "__main__":
    main()
