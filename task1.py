import random

# List of words for the game
words = ["python", "hangman", "developer", "programming", "challenge"]

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    word = random.choice(words)  # Select a random word
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit of incorrect guesses

    print("\nLet's play!")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        # Display the current state of the word
        print(display_word(word, guessed_letters))

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
