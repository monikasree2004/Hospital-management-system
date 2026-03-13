CREATE DATABASE hospital;

USE hospital;

CREATE TABLE patients(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
age INT,
disease VARCHAR(100)
);
SELECT*FROM patients;
INSERT INTO patients(name, age, disease) VALUES('John Doe', 30, 'Flu');