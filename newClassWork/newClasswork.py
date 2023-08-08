import mysql.connector as sql

import os


class Students:
    def __init__(self, first_name, number):
        self.first_name = first_name
        self.number = number

    def __str__(self):
        return "f{self.first_name},{self.number}"


class Db:
    def __init__(self):
        self._db = sql.connect(
            host="localhost",
            user="root",
            password="DexterJonson12%",
            database="syudentmanagementsystem"
        )
        self.present = "present"
        self.studentT = "student"
        self.cursor = self._db.cursor()

    def add_student(self, student):
        self.cursor.execute(
            f"INSERT INTO {self.studentT} (firstname, phone_number) values (%s,%s)", (student.first_name, student.number))
        self._db.commit()

    def all_students(self):
        self.cursor.execute(f"SELECT * FROM {self.studentT}")
        return self.cursor.fetchall()


class AttendanceSystem:
    def __init__(self):
        self.db = Db()

    def add_student_to_db(self, student):
        for _student in self.db.all_students():
            if _student[1] == student.first_name:
                print("this is an error")
        else:
            self.db.add_student(student)
            print("student added")


student1 = Students("dubem", "9066089664")

attendance = AttendanceSystem()
print(attendance.add_student_to_db(student1))
