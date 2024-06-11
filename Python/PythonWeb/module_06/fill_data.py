import sqlite3
from faker import Faker
import random


faker = Faker('uk-UA')


conn = sqlite3.connect('school.db')
cursor = conn.cursor()


for _ in range(3):
    cursor.execute('INSERT INTO groups (name) VALUES (?)', (faker.unique.word(),))


for _ in range(5):
    cursor.execute('INSERT INTO teachers (name) VALUES (?)', (faker.name(),))


cursor.execute('SELECT id FROM teachers')
teacher_ids = [row[0] for row in cursor.fetchall()]
for _ in range(8):
    cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (faker.unique.catch_phrase(), random.choice(teacher_ids)))


cursor.execute('SELECT id FROM groups')
group_ids = [row[0] for row in cursor.fetchall()]
for _ in range(50):
    cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (faker.name(), random.choice(group_ids)))


cursor.execute('SELECT id FROM students')
student_ids = [row[0] for row in cursor.fetchall()]
cursor.execute('SELECT id FROM subjects')
subject_ids = [row[0] for row in cursor.fetchall()]

for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(10, 20)):
            grade = random.randint(1, 12)
            date_received = faker.date_between(start_date='-1y', end_date='today')
            cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date_received))


conn.commit()
conn.close()
