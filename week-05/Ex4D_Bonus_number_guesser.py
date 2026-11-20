import time

# Create a pool of numbers using given number list
numbers = list(range(1, 50))

# Use a set as a second collection type
number_pool = set(numbers)

# Create a changing number based on the current time
secret_number = list(number_pool)[time.time_ns() % len(number_pool)]

# Track players guesses
guess_count = 0
guessed_numbers = []

# Display the possible range
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 50.")

# Keep asking until the correct guess
while True:

    # Ask the user for a guess
    guess_input = input("Enter your guess: ")

    # Check for non-numeric input
    try:
        guess = int(guess_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Count and save the guess
    guess_count += 1
    guessed_numbers.append(guess)

    # Give hints
    if guess < secret_number:
        print("Higher! Try again.")

    elif guess > secret_number:
        print("Lower! Try again.")

    else:
        print("Congratulations! You guessed correctly!")
        break

# Display final results
print("Total guesses:", guess_count)
print("Your guesses were:", guessed_numbers)

# Bonus message
if guess_count < 5:
    print("You're awesome!")
