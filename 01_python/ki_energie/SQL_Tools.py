import mysql.connector
import logging 


conn = ''

class select_Values() :
    pass
    
    
def connect_database() :
    global conn    
    conn = mysql.connector.connect(database='DeCarbonara',
                                            user='root',
                                        password='ia 2g 4ayh') 
    return

def db_conn():
    global conn
    return conn