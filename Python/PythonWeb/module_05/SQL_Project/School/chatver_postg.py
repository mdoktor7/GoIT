import psycopg2
from psycopg2 import sql
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
faker = Faker()

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="school_db",
    user="your_username",
    password="your_password",
    host="localhost"
)
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY(teacher_id) REFERENCES teachers(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES groups(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date_received DATE,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
)
''')

# Fill tables with random data using Faker
# Fill groups with unique names
for _ in range(3):
    group_name = faker.unique.company_suffix()
    cursor.execute('INSERT INTO groups (name) VALUES (%s)', (group_name,))

# Fill teachers
for _ in range(5):
    cursor.execute('INSERT INTO teachers (name) VALUES (%s)', (faker.name(),))

# Fill subjects with unique names
cursor.execute('SELECT id FROM teachers')
teacher_ids = [row[0] for row in cursor.fetchall()]
for _ in range(8):
    subject_name = faker.unique.catch_phrase()
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)', (subject_name, random.choice(teacher_ids)))

# Fill students
cursor.execute('SELECT id FROM groups')
group_ids = [row[0] for row in cursor.fetchall()]
for _ in range(50):
    cursor.execute('INSERT INTO students (name, group_id) VALUES (%s, %s)', (faker.name(), random.choice(group_ids)))

# Fill grades
cursor.execute('SELECT id FROM students')
student_ids = [row[0] for row in cursor.fetchall()]
cursor.execute('SELECT id FROM subjects')
subject_ids = [row[0] for row in cursor.fetchall()]

for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(10, 20)):
            grade = random.randint(1, 100)
            date_received = faker.date_between(start_date='-1y', end_date='today')
            cursor.execute('''
                INSERT INTO grades (student_id, subject_id, grade, date_received)
                VALUES (%s, %s, %s, %s)
            ''', (student_id, subject_id, grade, date_received))

# Commit changes and close connection
conn.commit()
conn.close()
