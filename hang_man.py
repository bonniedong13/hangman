""" 
This program plays hangman with the user. The computer will generate a random word 
from a file and give the user the number of letters. The user will try to guess the 
word by guessing what letters are in the word. 
"""
import random

def choosing_word():
    words = []
    # The words in this file are from https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/
    with open("hangman_words.txt") as file:
        for word in file:
            word = word.strip()
            words.append(word)
    return random.choice(words)

def check_guess_valid(already_guessed, guess):
    while True:
        if not(guess.isalpha()):
            guess = input("Please enter a letter: ")
        elif len(guess) > 1:
            guess = input("Please enter only one letter: ")
        elif guess in already_guessed:
            guess = input("You already guessed this. Choose another letter: ")
        else:
            break
    guess = guess.lower()
    return guess

def check_letter(word, player, letter):
    for index, char in enumerate(word):
        if char == letter:
            player[index] = letter
    return player

def check_completed_word(player):
    if "_" in player:
        return False
    else:
        return True

def hangman_drawing(lives_left):
    drawing = {10:f"  -----\n  |   |\n  |\n  |\n  |\n__|_____", 
    9:f"  -----\n  |   O\n  |\n  |\n  |\n__|____", 
    8:f"  -----\n  |   O\n  |   |\n  |\n  |\n__|_____", 
    7:f"  -----\n  |   O\n  |  /|\n  |\n  |\n__|_____",
    6:f"  -----\n  |   O\n  |  /|\ \n  |\n  |\n__|_____", 
    5:f"  -----\n  |   O\n  |  /|\ \n  |  /\n  |\n__|_____",
    4:f"  -----\n  |   O\n  |  /|\ \n  |  / \ \n  |\n__|_____", 
    3:f"  -----\n  |   O\n  |  /|\ \n  |  / \ \n  | -\n__|_____",
    2:f"  -----\n  |   O\n  |  /|\ \n  |  / \ \n  | -   -\n__|_____", 
    1:f"  -----\n  |   O\n  |  /|\ \n  |  / \ \n  | =   -\n__|_____",
    0:f"  -----\n  |   X\n  |  /|\ \n  |  / \ \n  | =   =\n__|_____"}
    for key in drawing:
        if key == lives_left:
            return drawing[key]
        

def main():
    # Setting up
    word = list(choosing_word())
    player_guess = []
    for i in range(len(word)):
        player_guess.append("_")
    print("".join(player_guess))

    # Player starts guessing the word
    lives = 10
    completed_word = False
    already_guessed = []
    while not(completed_word) and (lives > 0):

        # Get the user's guess and check for repetition or invalid guess
        guess = input("Enter a letter: ").lower()
        user_guess = check_guess_valid(already_guessed, guess)
        already_guessed.append(user_guess)

        # Check if the word was correct
        player_guess = check_letter(word, player_guess, user_guess)
        if user_guess not in word:
            lives = lives - 1
        
        # Print the data for user
        print(hangman_drawing(lives))
        print("Lives Left:", lives)
        print("Already Guessed:", ", ".join(already_guessed), f"")
        print("".join(player_guess))
    
        # Check if the player completed the word
        completed_word = check_completed_word(player_guess)

    # Print results
    if lives > 0:
        print("Congrats! You Win!")
    else:
        word = "".join(word)
        print(f"The word was '{word}'. Good luck next time.")

main()