DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student VARCHAR(50) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);

DROP TABLE IF EXISTS Groops;
CREATE TABLE Groops (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS Teachers;
CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher VARCHAR(50) NOT NULL,
);

DROP TABLE IF EXISTS Subjects;
CREATE TABLE Subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

DROP TABLE IF EXISTS Grades;
CREATE TABLE Grades (
    grade TINYINT UNSIGNED NOT NULL 
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);
