import mysql.connector
from mysql.connector import errorcode

def database_login ():
    config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': 'P!TV1p3r',
            'database': 'salespredictions',
    }
    
    try:
        db = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return print(f'you are now connected to the databased named: {database}')