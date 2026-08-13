


import json

students = []

file_name = "students.json"

try:
    with open(file_name, "r") as file:
        students = json.load(file)

        for student in students:
            student["skills"] = set(student["skills"])

except FileNotFoundError:
    students = []

while True :
    print("=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Student Result")
    print("5. Display Skills")
    print("6. Exit")




    choice = int(input("\nEnter Your Choice: "))

    while choice < 1 or choice > 6:
        print("Invalid choice. Please enter a number between 1 and 6.")
        choice = int(input("Enter Your Choice: "))




    match choice:


        case 1:

            print("\n========== ADD STUDENT ==========")

            student_id = int(input("Enter Student ID: "))

            while student_id <= 0:
                print("Student ID must be greater than 0.")
                student_id = int(input("Enter Student ID: "))

            for student in students:
                if student["id"] == student_id:
                    print("Student ID already exists.")
                    student_id = int(input("Enter a different Student ID: "))

            name = input("Enter Student Name: ")

            while not name.strip():
                print("Name cannot be empty.")
                name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))

            while age <= 0:
                print("Age must be greater than 0.")
                age = int(input("Enter Student Age: "))
            course = input("Enter Course: ")

            while not course.strip():
                print("Course cannot be empty.")
                course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))

            while marks < 0 or marks > 100:
                print("Marks must be between 0 and 100.")
                marks = float(input("Enter Marks: "))


            skills = {"Python", "SQL", "Excel"}

            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks,
                "skills": skills
            }

            students.append(student)

            students_for_json = []

            for student in students:

                student_copy = student.copy()

                student_copy["skills"] = list(student_copy["skills"])

                students_for_json.append(student_copy)

            with open(file_name, "w") as file:
                json.dump(students_for_json, file, indent=4)

            print("\nStudent Added Successfully!")
            



        case 2:

            print("\n========== VIEW STUDENTS ==========")

            if not students:

                print("No students found.")

            else:

                for student in students:

                    print("\nStudent ID:", student["id"])
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Course:", student["course"])
                    print("Marks:", student["marks"])


        case 3:

            print("\n========== SEARCH STUDENT ==========")

            search_id = int(input("Enter Student ID to Search: "))

            student_found = False

            for student in students:

                if student["id"] == search_id:

                    print("\nStudent Found!")

                    print("Student ID:", student["id"])
                    print("Name:", student["name"])
                    print("Age:", student["age"])
                    print("Course:", student["course"])
                    print("Marks:", student["marks"])

                    student_found = True

            if not student_found:
                print("\nStudent Not Found.")

        case 4:
            print("\n========== STUDENT RESULT ==========")

            search_id = int(input("Enter Student ID: "))

            student_found = False

            for student in students:

                if student["id"] == search_id:

                    marks = student["marks"]

                    if marks >= 90:
                        grade = "A+"
                    elif marks >= 80:
                        grade = "A"
                    elif marks >= 70:
                        grade = "B"
                    elif marks >= 60:
                        grade = "C"
                    elif marks >= 40:
                        grade = "D"
                    else:
                        grade = "Fail"

                    print("\nStudent Result")
                    print("-------------------------")
                    print("Student ID:", student["id"])
                    print("Name:", student["name"])
                    print("Course:", student["course"])
                    print("Marks:", marks)
                    print("Grade:", grade)

                    student_found = True

            if not student_found:
                print("\nStudent Not Found.")

        case 5:

            print("\n========== DISPLAY SKILLS ==========")

            search_id = int(input("Enter Student ID: "))

            student_found = False

            for student in students:

                if student["id"] == search_id:

                    print("\nStudent:", student["name"])
                    print("Skills:")

                    for skill in student["skills"]:
                        print("-", skill)

                    student_found = True

            if not student_found:
                print("\nStudent Not Found.")
        

        case 6:

            print("\nThank you for using Student Management System")
            break

        case _:

            print("\nInvalid choice")