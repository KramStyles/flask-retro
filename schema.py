from sqlite3 import connect, Error

connection = connect('flask_db.sql', check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username VARCHAR(50),
        password VARCHAR(400),
        fav_color VARCHAR(20)
    );
""")
connection.commit()

cursor.close()
connection.close()
