answer = r"6"

print("Welcome to the guessing game. Please take a guess between 1 - 10.")

while 1:
    guess = input("Enter your guess: ")
    if (guess == answer):
        print("Congratulations, {} is the correct guess!".format(guess))
        break
    elif (guess != answer):
        retry = input("WRONG! Do you wish to try again?: ")
        if (retry == "no"):
            break

print("thank you for playing the guessing game. Goodbye")
