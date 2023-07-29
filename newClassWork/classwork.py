class Student:
    def __init__(self, id: int, name: str, age: int) -> any:
        self.name = name
        self.age = age
        self.id = id

    def format_data(self):
        return f"{self.id},{self.name},{self.age}"


class StudentRecordManager:
    def add_student(self, student: Student) -> None:
        with open("student_record.txt", "a") as file:
            file.write(student.format_data() + "\n")

    def get_student(self, id: int) -> Student:
        with open("student_record.txt", "r") as file:
            record = file.readline()
            for rec in record:
                return rec`

student = Student(1, "dubem", 99)
manager = StudentRecordManager()
add_student = manager.add_student(student)

print(manager.get_student(1))
