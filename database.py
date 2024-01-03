import sqlite3
from datetime  import date

DB_NAME = 'Scoreboard.db'

def create_table():
    ''' Creates SQL tables to store user initials and score data '''

    # create DB connection
    con = sqlite3.connect(DB_NAME)
    # create DB cursor
    cur = con.cursor()
    try:
        cur.executescript('''CREATE TABLE IF NOT EXISTS scoreboard(
                          scoreID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                          initials TEXT(3) NOT NULL,
                          score INTEGER NOT NULL,
                          game_date TEXT);
                        ''')
        # commit to db
        con.commit()
        # display tables to console
        #read_sqlite_table()
    except sqlite3.Error as err:
        # log db error
        print(err)
        #db_logger.error(err)
    finally:
        if con:
            # close DB cursor
            cur.close()
            # close db connection
            con.close()

def add_score(initials, score):
    '''Append new user information into table if all inputs are valid
    :return: True if sign up successful, else False'''

     # create DB connection
    con = sqlite3.connect(DB_NAME)
    # create DB cursor
    cur = con.cursor()

    today = date.today()
    #format date month day, year
    f_date = today.strftime('%b %d, %Y')

    try:
        cur.execute('INSERT INTO scoreboard (initials, score, game_date) VALUES (?, ?, ?)',
                    (initials, score, f_date))
        con.commit()  # Commit the transaction
            #read_sqlite_table()
    except sqlite3.Error as err:
        # log error message
        print(err)
        # db_logger.error(err)
    finally:
        if con:
            # close DB cursor
            cur.close()
            con.close()