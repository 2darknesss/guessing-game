import random


def main():
    print("The game is started")

    num = random.randint(1,99)
    while True:     
        users_number = input("Guess the number: ")
        if users_number == 'exit':
            break
        elif users_number== 'is the number even':
            if num % 2 ==0 :
                print('The number is even')
            else:
                print("the number is odd ")
        elif num == users_number:
            print("You won")
        else: 
            print("You lose")

        
    

    # TODO: Features 
    # use loop
    # take input for finishing the game
    # take input for hint question 
    # add scoring mechanism 

    # TODO: Refactor
    # extract classes
    # use separate files



if __name__ == "__main__":
    main()
