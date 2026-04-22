import random
number = random.randint(1,1000)
while True:
    guess = int(input("Guess the number between 1,1000:"))
    if guess < number:
        print("Too low! Try again." \
        "Hint: The number is greater than your guess.")
    elif guess > number:
        print("too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break