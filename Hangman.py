import random
import json
import nltk
from nltk.corpus import words

def choose_word():
    english_words = random.choice(words.words())
    num_letters = len(english_words)
    return english_words, num_letters


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def hangman():
    word, num_letters = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(f"Number of letters: {num_letters}")
    print(display_word(word, guessed_letters))

    while '_' in display_word(word, guessed_letters) and incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_attempts - incorrect_guesses} attempts left.")
        print(display_word(word, guessed_letters))

    if '_' not in display_word(word, guessed_letters):
        print("Congratulations! You've guessed the word correctly.")
    else:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()


hangman()
