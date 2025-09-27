import random


HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']


WORDS_WITH_HINTS = {
    "python": "A popular programming language.",
    "elephant": "The largest land animal.",
    "guitar": "A musical instrument with strings.",
    "pizza": "An Italian dish with cheese and toppings.",
    "volcano": "A mountain that erupts lava."
}

def choose_word():
    word, hint = random.choice(list(WORDS_WITH_HINTS.items()))
    return word, hint

def display_progress(word, guessed_letters):
    display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    return display

def hangman():
    word, hint = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("Welcome to Hangman!")
    print("Hint:", hint)

    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", display_progress(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            wrong_guesses += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print(HANGMAN_PICS[wrong_guesses])
        print("Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
