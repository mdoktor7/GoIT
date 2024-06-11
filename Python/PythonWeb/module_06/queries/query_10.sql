SELECT subjects.name
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.student_id = %student_id% AND subjects.teacher_id = %teacher_id%
GROUP BY subjects.id;