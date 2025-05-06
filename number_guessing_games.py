import random

def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

def get_user_guess():
    while True:
        try:
            return int(input("Guess a number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")

def give_feedback(guess, secret_number, attempts):
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You won in {attempts} attempts!")
        return True
    
    # Give a hint after 3 wrong guesses
    if attempts == 3:
        if secret_number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    return False

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-50, unlimited guesses)")
    print("2. Medium (1-100, 10 guesses)")
    print("3. Hard (1-200, 5 guesses)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("Invalid choice!")

def ask_to_play_again():
    while True:
        choice = input("Play again? (y/n): ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        print("Please enter 'y' or 'n'.")

def play_game():
    difficulty = choose_difficulty()
    min_val, max_val, max_attempts = {
        1: (1, 50, float('inf')),
        2: (1, 100, 10),
        3: (1, 200, 5)
    }[difficulty]
    
    secret_number = generate_random_number(min_val, max_val)
    attempts = 0
    
    print(f"\nGuess a number between {min_val}-{max_val}.")
    
    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1
        
        if give_feedback(guess, secret_number, attempts):
            break  # Player guessed correctly
        
        remaining = max_attempts - attempts
        if remaining > 0 and max_attempts != float('inf'):
            print(f"{remaining} guesses left.")
    else:
        print(f"\nGame over! The number was {secret_number}.")

def main():
    """Entry point of the game."""
    print("Welcome to the Number Guessing Game!")
    while True:
        play_game()
        if not ask_to_play_again():
            print("\nThanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    main()