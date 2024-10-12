import time
import random
import string

def generate_random_word(length):
    letters = string.ascii_lowercase  # Use lowercase letters
    return ''.join(random.choice(letters) for _ in range(length))

def choose_word(l):
    # Generate a random word of the given length
    return generate_random_word(l)

def display_hangman(tries):
    stages = [
        """
      ------------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        """,
        """
      ------------
           |    |
           |    O
           |   /|\\
           |   /
           -
        """,
        """
      ------------
           |    |
           |    O
           |   /|
           |   
           -
        """,
        """
      ------------
           |    |
           |    O
           |    |
           |   
           -
        """,
        """
      ------------
           |    |
           |    O
           |   
           |   
           -
        """,
        """
      ------------
           |    |
           |    
           |   
           |   
           -
        """,
        """
      ------------
           |    
           |    
           |   
           |   
           -
        """,
    ]
    return stages[tries]

def play_hangman(length):
    word = choose_word(length)
    word_completion = "_ " * len(word)  # Create a string of underscores
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  # Number of tries based on hangman stages
    
    print(display_hangman(tries))
    print("Word to guess: " + word_completion)
    print("\n")

    while not guessed and tries > 0:
        print('guesses left' , tries)
        guess = input("Please guess a letter or word: ").lower()
        
        if len(guess) == 1:  # If the user guessed a letter
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(guess + " is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! " + guess + " is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word):  # If the user guessed the whole word
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(guess + " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Invalid guess.")

        print(display_hangman(tries))
        print("Word to guess: " + word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You've guessed the word! It was " + word + ".")
    else:
        print("Sorry, you've run out of tries. The word was " + word + ".")

if __name__ == '__main__':
    print(' -: Advanced Word Guessing Hangman Game :- ')
    name = input("What is your name? ")
    print("Hello, " + name + ", time to play hangman!")
    time.sleep(1)  # Pause for a second before starting
    length = int(input('Length of the guessing word: '))  # Ask for length here
    play_hangman(length)

