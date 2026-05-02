import subprocess
import sqlite3

# Vulnerability 1: SQL Injection
# AI loves writing queries this way - it's dangerous
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerability 2: Command Injection
# AI often uses subprocess with user input directly
def run_command(user_input):
    result = subprocess.run(user_input, shell=True)
    return result

# Vulnerability 3: Hardcoded password
# AI frequently hardcodes credentials
def connect_to_db():
    password = "admin123"
    host = "database.internal"
    return f"postgresql://admin:{password}@{host}/prod"
