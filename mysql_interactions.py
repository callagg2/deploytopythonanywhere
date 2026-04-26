import mysql.connector
from dbconfig import config_details


# this function will create the database if it doesn't already exist, this is useful for testing, 
# as it ensures that the database is there before we try to do any operations on it. 
# In a real application, you would probably want to have a separate script to set up the database and tables, 
# but for testing purposes, it's convenient to have this function in the DAO class.
def create_database():
    connection = mysql.connector.connect(
        host = config_details['host'],
        user = config_details['user'],
        password = config_details['password']   
          )
    try:
        sql = "Create database books1"
        values = ('books1',)
        cursor = connection.cursor()
        cursor.execute(sql)
        print("database created")
        cursor.close()
        connection.close()
    except mysql.connector.errors.DatabaseError as e:
        print(f"\nError creating database: {e}")

# this function will show the databases that exist, this is useful for testing
def show_databases():
    connection = mysql.connector.connect(
        host = config_details['host'],
        user = config_details['user'],
        password = config_details['password']   
          )
    try:
        sql = "Show databases"
        cursor = connection.cursor()
        cursor.execute(sql)
        databases = cursor.fetchall()
        for db in databases:
            print(db[0])
        cursor.close()
        connection.close()
    except mysql.connector.errors.DatabaseError as e:
        print(f"\nError showing databases: {e}")
        cursor.close()
        connection.close()

if __name__ == "__main__":
    show_databases()

# this function will create the books table if it doesn't already exist, this is useful for testing, 
# as it ensures that the table is there before we try to do any operations on it. 
# In a real application, you would probably want to have a separate script to set up the database and tables, 
# but for testing purposes, it's convenient to have this function in the DAO class.
def create_table():
    connection = mysql.connector.connect(
        host = config_details['host'],
        user = config_details['user'],
        password = config_details['password'],
        database = 'books1'
    )
    mycursor = connection.cursor()
    try:
        sql = "Create table if not exists books1 (id int primary key auto_increment, title varchar(255), author varchar(255), price int)"
        #values = ("books1",)
        mycursor.execute(sql)
        #mycursor.execute(sql, values) # we can use string formatting to insert the table name into the SQL statement, this is a good practice to avoid SQL injection attacks, and it also makes the code more flexible, as we can easily change the table name by changing the value in the config_details dictionary.
        connection.commit()
        print("table created")
        #print(f"table {values[0]} created")
        mycursor.close()
        connection.close()
    except mysql.connector.errors.DatabaseError as e:
        print(f"\nError creating table: {e}")
        mycursor.close()
        connection.close()

# this function will show the tables that exist, this is useful for testing
def show_tables():
    connection = mysql.connector.connect(
        host = config_details['host'],
        user = config_details['user'],
        password = config_details['password']   
          )
    try:
        sql0 = "Use books1"
        sql1 = "Show tables"
        cursor = connection.cursor()
        cursor.execute(sql0)
        cursor.execute(sql1)
        tables = cursor.fetchall()
        for table in tables:
            print(table[0])
        cursor.close()
        connection.close()
    except mysql.connector.errors.DatabaseError as e:
        print(f"\nError showing tables: {e}")
        cursor.close()
        connection.close()


def drop_table():
    connection = mysql.connector.connect(
        host = config_details['host'],
        user = config_details['user'],
        password = config_details['password'],
        database = 'books1'
    )
    mycursor = connection.cursor()
    try:
        sql = "Drop table if exists books1"
        #values = ('books1',)
        mycursor.execute(sql)
       #mycursor.execute(sql, values) # we can use string formatting to insert the table name into the SQL statement, this is a good practice to avoid SQL injection attacks, and it also makes the code more flexible, as we can easily change the table name by changing the value in the config_details dictionary.
        connection.commit()
        print("table dropped")
        #print(f"table {values[0]} dropped")
        mycursor.close()
        connection.close()
    except mysql.connector.errors.DatabaseError as e:
        print(f"\nError dropping table: {e}")
        mycursor.close()
        connection.close()

def drop_database():
    connection = mysql.connector.connect(
        host = config_details['host'],
        user = config_details['user'],
        password = config_details['password']   
          )
    try:
        sql = "Drop database if exists books1"
        # values = ('books1',)
        cursor = connection.cursor()
        cursor.execute(sql)
        # cursor.execute(sql,values) # we can use string formatting to insert the database name into the SQL statement, this is a good practice to avoid SQL injection attacks, and it also makes the code more flexible, as we can easily change the database name by changing the value in the config_details dictionary.  
        print("database dropped")
        # print(f"database {values[0]} dropped")
        cursor.close()
        connection.close()
    except mysql.connector.errors.DatabaseError as e:
        print(f"\nError dropping database: {e}")


if __name__ == "__main__":
#    create_database()
#    create_table()
#   show_databases()
#    show_tables()
#   drop_table()
   drop_database()