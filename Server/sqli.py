import sqlite3

# Create a SQLite database and a 'users' table
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create the 'users' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
