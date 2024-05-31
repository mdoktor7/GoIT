CREATE DATABASE School;

USE School;

-- Table of Students
CREATE TABLE Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student VARCHAR(50) NOT NULL,
    group_id INT,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);

-- Table of Groups
CREATE TABLE Groups (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

-- Table of Teachers
CREATE TABLE Teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher VARCHAR(50) NOT NULL,
    
);

-- Table of Subjects
CREATE TABLE Subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(50) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- Table of Grades
CREATE TABLE Grades (
    grade TINYINT UNSIGNED NOT NULL 
    date_received DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);
