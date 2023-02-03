from random import randint


numbers = randint(1, 100)

guessed = False


while not guessed:
    guess = input("Guess the number: ")
    try:
        num = int(guess)
        if num == numbers:
            print("You win!")
            guessed = True
        elif num > numbers:
            print("Too big!")
        else:
            print("Too small!")
    except ValueError:
        print("It's not a number!")
