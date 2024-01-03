from gamehelper import set_random_word, menu, add_leaderboard
from inputhandler import get_guess, play_again

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

                # earn 10 points for correct guess
                #set_score('+', 10)

                # if letter guessed correctly
                if guess in word_letters:
                    # remove - and replace with correct letter
                    word_letters.remove(guess)
                else:
                    print('Incorrect guess.')
                    # remove 1 life for incorrect guess
                    lives = lives - 1
                    # lose 10 points for incorrect guess
                    score = score + 10
                # if letter has already been guessed
            else:
                print('\nYou have already guessed that letter. Please try again.')
            # if user guesses entire word
        elif len(guess) > 1:
            # if word guess is incorrect
            if guess == random_word:
                print('You win!')
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