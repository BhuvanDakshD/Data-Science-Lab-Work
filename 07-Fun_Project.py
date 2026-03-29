import random

print(" Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")
print("You have 7 chances!\n")

# Generate random number
number = random.randint(1, 100)

chances = 7

for i in range(chances):
    print(f"\nAttempt {i+1} of {chances}")
    
    guess = int(input("Enter your guess: "))

    if guess < number:
        print(" Too low! Try again.")
    elif guess > number:
        print(" Too high! Try again.")
    else:
        print(" Congratulations! You guessed the correct number!")
        break
else:
    print("\n You lost!")
    print("The correct number was:", number)
