''' Module with functions that handle/validate user input '''

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
              # initials must be 3 char in length
            if len(initials) == 3:
                # validate input
                if validate_input(initials):
                    return initials
            else:
                print('Initials must be three characters.')
                continue
        except ValueError:
            print('Invalid input.')
