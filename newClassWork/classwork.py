class Student:
    def __init__(self, id: int, name: str, age: int) -> any:
        self.id = id
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.id, self.name, self.age}"


class StudentRecordManager:
    def add_student(self, student: Student) -> None:
        stunt_infi = {}
        with open("student_record.txt", "a") as file:
            # stunt_infi[student.id] = student
            file.write(student + "\n")

    def get_student(id: int) -> str:
        with open("student_record.txt", "r") as file:
            if str(id) in file.read():
                return id
            else:
                return "none"


manager = StudentRecordManager()

student1 = Student(3, "david", 20)

manager.add_student(str(student1))


print(StudentRecordManager.get_student(3))
