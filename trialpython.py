import random

print("Welcome to the Number Guessing Game!")

number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Enter your guess (1-20): "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it!")
        break

print("Number was:", number)
print("Total attempts:", attempts)
print("Thanks for playing!")
