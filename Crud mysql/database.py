import pymysql
 
def get_connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )
    print("connect")
    return conn

def create_table():
    conn = get_connect()
    cursor = conn.cursor()
    
    cursor.execute(CREATE TABLE studen)