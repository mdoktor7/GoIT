-- query_1.sql
Знайти 5 студентів із найбільшим середнім балом з усіх предметів:
SELECT students.id, students.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 5;


-- query_2.sql
Знайти студента із найвищим середнім балом з певного предмета:
SELECT students.id, students.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math') -- Замінити 'Math' на потрібний предмет
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;

-- query_3.sql
Знайти середній бал у групах з певного предмета:
SELECT groups.id, groups.name, AVG(grades.grade) as average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math') -- Замінити 'Math' на потрібний предмет
GROUP BY groups.id;

-- query_4.sql
Знайти середній бал на потоці (по всій таблиці оцінок):
SELECT AVG(grade) as average_grade
FROM grades;

-- query_5.sql
Знайти які курси читає певний викладач:
SELECT subjects.name
FROM subjects
WHERE teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe'); -- Замінити 'John Doe' на потрібного викладача

-- query_6.sql
Знайти список студентів у певній групі:
SELECT students.id, students.name
FROM students
WHERE group_id = (SELECT id FROM groups WHERE name = 'Group A'); -- Замінити 'Group A' на потрібну групу

-- query_7.sql
Знайти оцінки студентів у окремій групі з певного предмета:
SELECT students.id, students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = (SELECT id FROM groups WHERE name = 'Group A') -- Замінити 'Group A' на потрібну групу
AND grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math'); -- Замінити 'Math' на потрібний предмет

-- query_8.sql
Знайти середній бал, який ставить певний викладач зі своїх предметів:
SELECT AVG(grades.grade) as average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE subjects.teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe'); -- Замінити 'John Doe' на потрібного викладача

-- query_9.sql
Знайти список курсів, які відвідує студент:
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = (SELECT id FROM students WHERE name = 'Jane Doe'); -- Замінити 'Jane Doe' на потрібного студента

-- query_10.sql
Список курсів, які певному студенту читає певний викладач:
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = (SELECT id FROM students WHERE name = 'Jane Doe') -- Замінити 'Jane Doe' на потрібного студента
AND subjects.teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe'); -- Замінити 'John Doe' на потрібного викладача

Додаткові Запити

-- query_11.sql
Середній бал, який певний викладач ставить певному студентові:
SELECT AVG(grades.grade) as average_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = (SELECT id FROM students WHERE name = 'Jane Doe') -- Замінити 'Jane Doe' на потрібного студента
AND subjects.teacher_id = (SELECT id FROM teachers WHERE name = 'John Doe'); -- Замінити 'John Doe' на потрібного викладача


-- query_12.sql
Оцінки студентів у певній групі з певного предмета на останньому занятті:
SELECT students.id, students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = (SELECT id FROM groups WHERE name = 'Group A') -- Замінити 'Group A' на потрібну групу
AND grades.subject_id = (SELECT id FROM subjects WHERE name = 'Math') -- Замінити 'Math' на потрібний предмет
AND grades.date_received = (
    SELECT MAX(date_received)
    FROM grades
    WHERE subject_id = (SELECT id FROM subjects WHERE name = 'Math') -- Замінити 'Math' на потрібний предмет
    AND student_id = students.id
);
