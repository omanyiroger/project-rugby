import sqlite3
from werkzeug.security import generate_password_hash

# Connect to your database
conn = sqlite3.connect('your_database.db')  # replace with your actual DB path
cursor = conn.cursor()

# Sample users
users = [
    ('coach1', generate_password_hash('coachpass'), 'coach'),
    ('physio1', generate_password_hash('physiopass'), 'physio'),
    ('player1', generate_password_hash('playerpass'), 'player')
]

# Insert users into the table
for username, password, role in users:
    try:
        cursor.execute('INSERT INTO user_roles (username, password, role) VALUES (?, ?, ?)',
                       (username, password, role))
    except sqlite3.IntegrityError:
        print(f"User {username} already exists.")

conn.commit()
conn.close()