import requests
import sqlite3

API_URL = "https://hackbulgaria.com/api/students/"
data = requests.get(API_URL).json()

with open("API_content_HR", "w") as f:
    f.write(str(data))


conn = sqlite3.connect("hr.db")
cursor = conn.cursor()

course_name_to_id = {}


def create_student(conn, cursor, student):
    cursor.execute("""DELETE FROM Students""")
    insert_query = """
    INSERT INTO students(name, github)
    VALUES(?, ?)
    """
    cursor.execute(insert_query, (student["name"], student["github"]))
    conn.commit()
    return cursor.lastrowid


def create_course(conn, cursor, course):
    cursor.execute("""DELETE FROM courses""")
    insert_query = """
    INSERT INTO courses(name)
    VALUES(?)
    """
    cursor.execute(insert_query, (course["name"],))
    conn.commit()
    return cursor.lastrowid


def create_relation(conn, cursor, student_id, course_id):
    cursor.execute("""DELETE FROM students_to_courses""")
    insert_query = """
    INSERT INTO students_to_courses(student_id, course_id)
    VALUES(?, ?)
    """
    cursor.execute(insert_query, (student_id, course_id))
    conn.commit()
    return cursor.lastrowid

create_students = """
CREATE TABLE IF NOT EXISTS students
(student_id INTEGER PRIMARY KEY,
    name TEXT,
    github TEXT)
"""
create_courses = """
CREATE TABLE IF NOT EXISTS courses
(course_id INTEGER PRIMARY KEY,
    name TEXT)
"""
students_to_courses = """
CREATE TABLE IF NOT EXISTS students_to_courses(
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(course_id) REFERENCES courses(course_id))
    """
for table in [create_students, create_courses, students_to_courses]:
    cursor.execute(table)
    conn.commit()

for student in data:
    student_id = create_student(conn, cursor, student)
    courses = student["courses"]

    for course in courses:
        course_name = course["name"]

        if course_name in course_name_to_id:
            course_id = course_name_to_id[course_name]
        else:
            course_id = create_course(conn, cursor, course)
            course_name_to_id[course_name] = course_id
        create_relation(conn, cursor, student_id, course_id)
