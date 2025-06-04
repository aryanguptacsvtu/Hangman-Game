import random
from colorama import Fore, Style, init

init(autoreset=True)

words = ["UNICORN", "PYTHON", "COMPUTER", "PROGRAMMING", "DEVELOPER",
         "CLASS", "METHOD", "INHERITANCE", "ENCAPSULATION",
         "FUNCTION", "VARIABLE", "OBJECT", "INSTANCE", "ATTRIBUTE",
         "POLYMORPHISM", "ABSTRACTION", "DEBUGGING", "ERROR",
         "EXCEPTION", "LIBRARY", "MODULE", "PACKAGE"]

# Hangman visual stages (from 7 lives down to 0)
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    ---------
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    ---------
    """
]

# Main game loop
while True:
    
    word = random.choice(words)
    total_chances = 7
    guessed_word = "_" * len(word)

    print(Fore.CYAN + "\n🎉 Welcome to Hangman Game! 🎉")

    while (total_chances != 0):

        print(hangman_stages[7 - total_chances])
        print("\n" + " ".join(guessed_word))
        letter = input(Fore.YELLOW + "🔤 Guess a letter: ").upper()

        # If guessed letter is in the word
        if letter in word:

            # Reveal the letter in the guessed word
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_word = guessed_word[:i] + letter + guessed_word[i+1:]

            if guessed_word == word:
                print(Fore.GREEN + "🎉 Congratulations! You guessed the word: " + word + " 🎯")
                break

        # If guessed letter is not in the word
        else:
            total_chances -= 1
            print(Fore.RED + f"❌ Wrong guess! You have {total_chances} chances left. 💀")
     
    # If loop ends and player hasn't guessed the word
    else:
        print(hangman_stages[-1])
        print(Fore.RED + "💀 Game Over! You LOSE!!")
        print(Fore.RED + "📌 The word was: " + word)

    # Ask to play again
    play_again = input(Fore.CYAN + "\n🔁 Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print(Fore.MAGENTA + "👋 Thanks for playing! See you next time!")
        break
