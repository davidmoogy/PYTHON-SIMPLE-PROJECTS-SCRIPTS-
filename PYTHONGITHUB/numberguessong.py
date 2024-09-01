import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

    # Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        number_guessing_game()

if __name__ == "__main__":
    number_guessing_game()
