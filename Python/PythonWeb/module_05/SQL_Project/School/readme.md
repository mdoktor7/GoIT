Explanation:
Students Table:

student_id: Unique identifier for each student.
first_name: First name of the student.
last_name: Last name of the student.
date_of_birth: Date of birth of the student.
group_id: Foreign key referencing the Groups table.
Groups Table:

group_id: Unique identifier for each group.
group_name: Name of the group.
Teachers Table:

teacher_id: Unique identifier for each teacher.
first_name: First name of the teacher.
last_name: Last name of the teacher.
Subjects Table:

subject_id: Unique identifier for each subject.
subject_name: Name of the subject.
teacher_id: Foreign key referencing the Teachers table.
Grades Table:

grade_id: Unique identifier for each grade entry.
student_id: Foreign key referencing the Students table.
subject_id: Foreign key referencing the Subjects table.
grade: The grade received by the student (0.00 to 100.00).
date_received: The date when the grade was received.
Additional Notes:
Foreign key constraints ensure referential integrity between the tables.
The Grades table uses a DECIMAL type for the grade column to handle grades with decimal points.
Check constraints ensure that grades are within the valid range (0.00 to 100.00).
This schema can be further expanded or modified based on additional requirements, such as handling multiple groups per student, more detailed teacher and student information, or additional attributes for subjects and grades.
