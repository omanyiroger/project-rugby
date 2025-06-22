
from flask_login import UserMixin
import sqlite3

class User(UserMixin):
    def _init_(self, id, email, password, role):
        self.id = id
        self.email = email
        self.password = password
        self.role = role

    def check_password(self, input_password):
        return self.password == input_password  # You can add hashing later
        

def get_user_by_email(email):
    conn = sqlite3.connect("rcmis.db")
    cur = conn.cursor()
    cur.execute("SELECT id, email, password, role FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None

def get_user_by_id(user_id):
    conn = sqlite3.connect("rcmis.db")
    cur = conn.cursor()
    cur.execute("SELECT id, email, password, role FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(*row)
    return None