''' Module with functions that handle/validate user input '''

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

def has_numbers(strng):
    ''' function to determine if input contains any numbers in string
    :return: True if numbers in string, else False '''
    return any(char.isdigit() for char in strng)

def validate_input(strng):
    ''' function for validating user input for guess variable
    :return: True if valid, else False '''
    #define special characters
    special_characters = '!@#$%^&*()-+?_=,<>/"'
    #check if input is blank
    if strng == '':
        print('Input cannot be blank.')
    #check if input is numerical
    elif strng.isnumeric():
        print('Input cannot be numerical.')
    #check if input contains numbers
    elif has_numbers(strng):
        print('Input may not contain numbers.')
    #check if input contains any special characters
    elif any(c in special_characters for c in strng):
        print('Input cannot contain any special characters')
    else:
        #return true if input is valid
        return True
    #invalid input, return false
    return False
    
def set_initials():
    ''' Method to get and validate user initals as input  '''
    # loop to get input
    while True:
        try:
            initials = input("Enter initials: ").strip().upper()
        except ValueError:
            print('Invalid input.')
        
        # initials must be 3 char in length
        if len(initials) > 3 or len(initials) < 3:
            print('Initials must be three characters.')
        else:
            # validate input
            if validate_input(initials):
                return initials
            
def get_guess():
    while True:
            try:
                guess = input('\nGuess a letter or word: ').strip().lower()
                break
            except ValueError:
                print('Invalid input')
                continue
    
    if validate_input(guess):
        return guess

