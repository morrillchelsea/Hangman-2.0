from game import validate_input

def set_score(op, points):
    ''' Method to handle addition or deduction of points based on correctness of user guess '''
    if op == '+':
        self.score = self.score + points
    else:
        self.score = self.score - points

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

def win():
    ''' Method to handle if user wins the game '''
    # add 100 points to score for user win
    set_score('+', 100)
    # print winner message
    print('You win!')
    # output final score to user
    #print(f'Score: {score}')
    
    #prompt user to add initials to leaderboard
    if add_leaderboard():
        # get initials as input and assign to var
        initials = set_initials()
        # add items to DynamoDB leaderboard
        #add_items(initials, score)

def lose():
    ''' Method to handle if user loses the game '''
    # subtract 50 points for loss
    set_score('-', 50)
    # output final score to user
    #print(f'Score: {get_score()}')
    # game is over
    print('Game over!')

def add_leaderboard():
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
            return True
        elif c == 'n':
            return False
        else:
            print('Error: Please enter y or n.')
