 
import random
import string


def hangman():
    # List of words for the game
    word_list = ["python", "hangman", "programming", "computer", "keyboard",
                 "developer", "algorithm", "function", "variable", "string"]

    # Select a random word from the list
    secret_word = random.choice(word_list).lower()
    letters_guessed = []
    attempts_remaining = 6  # Typically 6 attempts in hangman

    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")

    while True:
        # Display current progress
        display_word = ""
        for letter in secret_word:
            if letter in letters_guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        # Check if player has won
        if all(letter in letters_guessed for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

        # Check if player has lost
        if attempts_remaining <= 0:
            print("Game over! You ran out of attempts.")
            print("The word was:", secret_word)
            break

        # Get player's guess
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif guess not in string.ascii_lowercase:
                print("Please enter a valid letter.")
            elif guess in letters_guessed:
                print("You've already guessed that letter. Try again.")
            else:
                break

        letters_guessed.append(guess)

        # Check if guess is correct
        if guess not in secret_word:
            attempts_remaining -= 1
            print(f"Wrong guess! You have {attempts_remaining} attempts remaining.")
            print_hangman(attempts_remaining)


def print_hangman(attempts):
    # Simple ASCII art for hangman
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    print(stages[6 - attempts])


if __name__ == "__main__":
    hangman()