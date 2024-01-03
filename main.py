'''
Created by: Nieves, Chelsea
SDEV400
Prof Craig Poma
Last Modified: 3 Jan 2024

'''
from game import menu
from database import create_table

def main():
    # call database.py method create_table() to create leaderboard with SQLite3
    create_table()
    
    # call menu function from Menu class
    menu()

# Call main function
if __name__ == '__main__':
    main()
