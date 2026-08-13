# Student Management System

## 📌 Project Overview

A console-based Student Management System built using Python.

This project combines the Python concepts learned during the first 10 days of learning and applies them to a practical application.

The system allows users to add, view, search, and manage student information through a menu-driven interface.

---

## 🚀 Features

- Add Student
- View All Students
- Search Student by ID
- Calculate Student Grade
- Display Student Skills
- Prevent Duplicate Student IDs
- Validate Student ID
- Validate Student Name
- Validate Student Age
- Validate Course
- Validate Marks
- Store student data in JSON
- Load saved data when the program starts
- Menu-driven interface

---

## 🧠 Python Concepts Used

- Variables
- Data Types
- Type Casting
- Strings
- Lists
- Tuples
- Sets
- Dictionaries
- Operators
- `if / elif / else`
- `match / case`
- `while` loop
- `for` loop
- `break`
- `continue`
- User Input
- File Handling
- JSON
- Basic Input Validation

---

## 📂 Project Structure

```text
StudentManagementSystem/
│
├── Stud_Management.py
├── students.json
├── README.md
└── output.txt
```

---

## 👨‍🎓 Student Information

Each student contains:

- Student ID
- Name
- Age
- Course
- Marks
- Skills

Example:

```python
student = {
    "id": 1001,
    "name": "Chandan",
    "age": 26,
    "course": "Python",
    "marks": 69.0,
    "skills": {"Python", "SQL", "Excel"}
}
```

---

## 📊 Grade System

| Marks | Grade |
|---:|---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 40–59 | D |
| Below 40 | Fail |

---

## 💾 Data Storage

Student information is stored in:

```text
students.json
```

JSON allows the application to preserve student information even after the program is closed.

When the program starts, existing student records are loaded from the JSON file.

---

## ▶️ How to Run

Make sure Python is installed.

Run:

```bash
python Stud_Management.py
```

Or using Python 3:

```bash
python3 Stud_Management.py
```

---

## 🖥️ Main Menu

```text
==================================================
        STUDENT MANAGEMENT SYSTEM
==================================================

1. Add Student
2. View Students
3. Search Student
4. Student Result
5. Display Skills
6. Exit
```

---

## 🎯 Learning Outcome

This project demonstrates how individual Python concepts can be combined to create a practical console-based application.

It was developed as part of my Python learning journey in Data Science.

---

## 👤 Author

**Chandan B**

Data Science | Python | SQL | Excel | Power BI
