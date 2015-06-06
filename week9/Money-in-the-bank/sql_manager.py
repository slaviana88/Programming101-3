import sqlite3
import uuid
import hashlib
import re
import getpass
from Client import Client
from settings import DB_NAME, SQL_FILE

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

UPDATE_SQL = """UPDATE clients
                SET message = ?
                WHERE id = ?
"""

UPDATE_SQL2 = """UPDATE clients
                 SET password = ?
                 WHERE id = ?
"""

INSERT_SQL = """ INSERT INTO clients (username, password)
                 VALUES (?,?)
"""

SELECT_QUERY = """ SELECT id, username, balance, message
                   FROM clients
                   WHERE username = ? AND password = ?
                   LIMIT 1
"""

SELECT_PASSWORD = """ SELECT password
                      FROM clients
                      WHERE username = ?
"""


def create_clients_table():
    with open(SQL_FILE, "r") as f:
        conn.executescript(f.read())
        conn.commit()


def change_message(new_message, logged_user):
    cursor.execute(UPDATE_SQL, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def hash_password(password):
    # uuid is used to generate a random number
    random_number = uuid.uuid4().hex
    hashable = hashlib.sha256(random_number.encode() + password.encode()).hexdigest()
    return hashable + ':' + random_number


def change_pass(new_pass, logged_user):
    cursor.execute(UPDATE_SQL2, (new_pass, logged_user.get_id()))
    conn.commit()


def check_password(password):
    if not any(x.isupper() for x in password):
        print("Enter capital letter!")
    if not any(x.islower() for x in password):
        print("Enter lower letter!")
    if not any(x.isdigit() for x in password):
        print("Enter number!")
    if len(password) <= 8:
        print("Enter password with more than 7 letters!")
    # if not re.match(r"[^0-9a-zA-Z\s]", password):
    #     print("Invalid entry.")


def register(username, password):
    password = password.strip()
    while not check_password(password):
        password = getpass.getpass("Try again: ", stream=None)
    password = hash_password(password)
    cursor.execute(INSERT_SQL, (username, password))
    conn.commit()


def check_hash_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def login(username, password):
    cursor.execute(SELECT_PASSWORD, (username,))
    hash_pass = cursor.fetchone()[0]
    if check_hash_password(hash_pass, password):
        password = hash_pass
        cursor.execute(SELECT_QUERY, (username, password))
        user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False

