SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = %group_id% AND grades.subject_id = %subject_id%;