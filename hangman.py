import random
import sys
from database import view_my_scores, view_top_scoreboard, add_score
from handler import validate_input, set_initials

def play_again():
    ''' method to handle if user wants to play the game again
    :return: True if yes, False if no'''
    while True:
        try:
            #prompt user to search for additional course titles
            c = input('Play again? y = Yes n = No (Return to Main Menu): ').strip().lower()
        except ValueError:
            print('Invalid entry.')
            continue
        if c == 'y':
            return True
        elif c == 'n':
            return False
        else:
            print('Error: Please enter y or n.')

def get_guess():
    ''' Method to handle getting user guess input for gameplay
    :return: guess'''
    while True:
            try:
                guess = input('\nGuess a letter or word: ').strip().lower()
                if validate_input(guess):
                    return guess
            except ValueError:
                print('Invalid input')
                continue

def add_leaderboard(score):
    ''' method to handle if user wants to play the game again
    :return: True if yes, False if no'''
    while True:
        try:
            #prompt user to search for additional course titles
            c = input('Add name to leaderboard? y = Yes n = No: ').strip().lower()
            
            if c == 'y':
                initials = set_initials()
                add_score(initials, score)
                break
            elif c == 'n':
                break
            else:
                print('Error: Please enter y or n.')
        except ValueError:
            print('Invalid entry.')

def set_random_word():
    ''' read file from S3 bucket and output random word to be guessed 
    :return: random_word'''
    words = []
    try:  
        with open ('hangman_dictionary.txt', 'r', encoding = 'utf-8') as file:
        #with open ('Untitled.txt', 'r', encoding = 'utf-8') as file:
            lines = file.read().splitlines()
            for word in lines:
                words.append(word)
    except IOError as err:
        print(err)

    # assign random string to variable
    random_word = random.choice(words)

    return random_word

# menu option 0
def exit_handler():
    '''Prints message thanking user for playing and exits program'''
    print('\n-------------------------------------------')
    print('\nThank you for playing!')
    print('Exiting program.')
    print('\n-------------------------------------------')
    sys.exit()

# menu option 1
def new_game():
    ''' method to play new game of hangman '''
    # assign a random word from dictionary.txt to random_word variable
    random_word = set_random_word()
    # create a set of letters in random_word
    word_letters = set(random_word)
    # set of letters the user has previously guessed
    letters_guessed = set()
    # user begins with 6 lives
    lives = 6
    # var for user's guess
    guess = ''
    # user begins each game with 0 points
    score = 0

    while lives > 0 and len(word_letters) > 0 and guess != random_word:
        print('\n-------------------------------------------')
        #output lives left
        print(f'\nYou have {lives} lives left.')
        # output current score
        print(f'Score: {score}')
        #output letters guessed
        print('Guessed letters:', ','.join(letters_guessed))
        print('\n-------------------------------------------')

        # prints letter in random_word if previously guessed
        # else print -
        # (ie w - r d)
        word_list = [letter if letter in letters_guessed
                else '-' for letter in random_word]

        print('\n', ' '.join(word_list))

        guess = get_guess()

        # if user guesses a single letter in the word
        if len(guess) == 1:
            # if letter has not been guessed previously
            if guess not in letters_guessed:
                # append letter to letters_guessed set
                letters_guessed.add(guess)

                # if letter guessed correctly
                if guess in word_letters:
                    # remove - and replace with correct letter
                    word_letters.remove(guess)
                    # earn 10 points for correct guess
                    score = score + 10
                else:
                    print('Incorrect guess.')
                    # remove 1 life for incorrect guess
                    lives = lives - 1
                    # lose 10 points for incorrect guess
                    score = score - 10
            # else letter has already been guessed
            else:
                print('\nYou have already guessed that letter. Please try again.')
        # if user guesses entire word
        elif len(guess) > 1:
            # if word guess is incorrect
            if guess == random_word:
                break
            else:
                print('Incorrect guess.')
                # remove 1 life for incorrect guess
                lives = lives - 1
    # break out of while loop            
    # if user is out of lives
    if lives == 0:
        # print word
        print(f'Sorry, you lose. The word was: {random_word}')
        ''' Method to handle if user loses the game '''
        # subtract 50 points for loss
        score = score - 50
        # output final score to user
        print(f'Score: {score}')
        # game is over
        print('Game over!')
    else:
        # print word
        print(f'You have correctly guessed: {random_word}')
        # add 100 points to score for user win
        score = score + 100
        # print winner message
        print('You win!')
        # output final score to user
        print(f'Score: {score}')
        add_leaderboard(score)

    # check if user wants to play again
    if play_again():
        # begin a new game
        new_game()
    else:
        # return to main menu
        menu()
 
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

def menu_handler(choice):
    ''' function to handle menu option choice '''
    # create instance of class Hangman
    if choice == 1:
        # play game
        new_game()
    elif choice == 2:
        # view scoreboard
        view_my_scores(set_initials())
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
        print('\nInvalid selection')

def menu():
    ''' method to output menu options to user and accept user input '''
    # print welcome message
    print('\n-------------------------------------------')
    print('\nMain Menu')
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
