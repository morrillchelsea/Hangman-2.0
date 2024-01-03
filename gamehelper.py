import random
import sys
from hangman import new_game
from database import view_top_scoreboard, view_my_scores, add_score
from inputhandler import set_initials

def set_random_word():
    ''' read file from S3 bucket and output random word to be guessed 
    :return: random_word'''
    words = []
    try:  
        #with open ('hangman_dictionary.txt', 'r', encoding = 'utf-8') as file:
        with open ('Untitled.txt', 'r', encoding = 'utf-8') as file:
            lines = file.read().splitlines()
            for word in lines:
                words.append(word)
    except IOError as err:
        print(err)

    # assign random string to variable
    random_word = random.choice(words)

    return random_word

def add_leaderboard(score):
    ''' method to handle if user wants to play the game again
    :return: True if yes, False if no'''
    while True:
        try:
            #prompt user to search for additional course titles
            c = input('Add name to leaderboard? y = Yes n = No: ').strip().lower()
        except ValueError:
            print('Invalid entry.')
            continue
        if c == 'y':
            initials = set_initials()
            add_score(initials, score)
        elif c == 'n':
            return False
        else:
            print('Error: Please enter y or n.')

# menu option 4
def display_rules():
    ''' Prints rules to user
    Obtained from https://en.wikipedia.org/wiki/Hangman_(game) '''
    rules = '''
    The word to guess is represented by a row of dashes representing each letter of the word.
    Proper nouns, such as names, places, brands, or slang are forbidden. If the guessing player 
    suggests a letter which occurs in the word, the letter will appear in all of its correct
    positions and 10 points are added to the score. If the suggested letter does not occur in the
    word or the word is guessed incorrectly, a life is removed and 10 points are deducted from the
    score. The game ends once the word is guessed, or if all of the lives are gone, signifying that
    all guesses have been used. Winning by guessing each character individually earns the user 100
    points. The player guessing the word may, at any time, attempt to guess the whole word. If the
    word is correct, 150 points are earned, the game is over and the guesser wins. Otherwise, a
    life is removed.
    '''
    print('\n-------------------------------------------')
    print('\nHow to Play: ')
    print('\n-------------------------------------------')
    print(rules)

# menu option 0
def exit_handler():
    '''Prints message thanking user for playing and exits program'''
    print('\n-------------------------------------------')
    print('\nThank you for playing!')
    print('Exiting program.')
    print('\n-------------------------------------------')
    sys.exit()

def menu_handler(choice):
    ''' function to handle menu option choice '''
    # create instance of class Hangman
    if choice == 1:
        # play game
        new_game()
    elif choice == 2:
        # view scoreboard
        view_my_scores(set_initials())
        return
    elif choice == 3:
        # display leadrboard
        view_top_scoreboard()
    elif choice == 4:
        # display game rules
        display_rules()
    elif choice == 0:
        # exit program
        exit_handler()
    else:
        # choice not acceptable menu option
        print('Invalid selection')

def menu():
    ''' method to output menu options to user and accept user input '''
    # print welcome message
    print('\n-------------------------------------------')
    print('\nWelcome to Hangman!')
    print('\n-------------------------------------------')

    # loop to get user input
    while True:
        # print menu options
        print('\nPlease select an option from the menu below: ')
        print('1. New Game')
        print('2. View My Scores')
        print('3. View Scoreboard')
        print('4. How to Play')
        print('0. Exit Game')

        try:
            # get user input
            choice = int(input('Menu option: '))
            # if user input is valid
            if len(str(choice)) > 1:
                print('Menu selection cannot contain more than one digit')
            elif choice < 0:
                print('Menu option cannot be a negative number')
            # input is valid
            else:
                # assign input to self.choice
                menu_handler(choice)
        except ValueError:
            # choice not acceptable menu option
            print('\nInvalid selection.')
            continue

