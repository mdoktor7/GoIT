import sqlite3


conn = sqlite3.connect('school.db')
cursor = conn.cursor()


with open('school.sql', 'r') as file:
    cursor.executescript(file.read())


conn.commit()
conn.close()
