from login import show_login
import sqlite3

# Andre Carbajal
def create_user_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)
    ''', ('user@example.com', 'password123'))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_user_database()
    show_login()