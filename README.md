#  Student Management System (Flask + MySQL)

A full-stack **Student CRUD (Create, Read, Update, Delete)** web application built using **Flask (Python)** for the backend and **MySQL** for data storage. The frontend is a clean HTML + JavaScript interface (no Bootstrap or frameworks).

---

## Features

- Add new students
- View all students
- Update existing student records
- Delete students by ID
- Pure HTML + JS frontend (no libraries)
- Fully connected with MySQL backend

---

##  Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Frontend     | HTML, CSS, JavaScript |
| Backend      | Flask (Python)   |
| Database     | MySQL            |

---


---

## Setup Instructions

1. Clone the Repository
   
git clone https://github.com/yourusername/student-crud-flask.git
cd student-crud-flask
2. Install Python Dependencies

pip install flask mysql-connector-python
3.Set Up MySQL Database
Open your MySQL client (e.g., MySQL Shell, Workbench) and run:

CREATE DATABASE mydatabase;

USE mydatabase;

CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  mark INT
);
4.Run the Flask App

python app.py

## Future Improvements
Form validation
User login system
Responsive UI
React frontend

## Author
Jayasri M.B.
B.Tech Artificial Intelligence and Machine Learning
RMD Engineering College

## License
This project is open-source and free to use for educational purposes.
