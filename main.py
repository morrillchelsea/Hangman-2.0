'''
Created by: Nieves, Chelsea
SDEV400
Prof Craig Poma
Last Modified: 3 Jan 2024

'''
from hangman import menu
from database import create_table

def main():
    # call database.py method create_table() to create leaderboard with SQLite3
    create_table()
    print('\nWelcome to Hangman!')
    # call menu function from Menu class
    menu()

# Call main function
if __name__ == '__main__':
    main()
