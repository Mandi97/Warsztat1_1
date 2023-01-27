from random import randint

# chosing a random number from 1 to 100
numbers = randint(1, 101)

guessed = False

# checking if user wrote a number
# and if this number is the number our randint option chose

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
