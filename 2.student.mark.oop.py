class Student:
    def __init__(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.dob = input("Enter student date of birth: ")
        self.marks = {}

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_dob(self, dob):
        self.dob = dob

    def set_mark(self, course, mark):
        self.marks.update({course: mark})

    def displayStudent(self):
        print("Student ID: " + self.id)
        print("Student name: " + self.name)
        print("Student DoB: " + self.dob)
        print("-------")

    def displayMark(self, course):
        print(self.name + "'s mark: " + str(self.marks.get(course)))


class Course:
    def __init__(self):
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def displayCourse(self):
        print("Course ID: " + self.id)
        print("Course name: " + self.name)
        print("-------")


def numOfStudent():
    while True:
        try:
            std_num = int(input("Enter number of student in the class: "))
            print("-------")
            return std_num
        except ValueError:
            print("Invalid number.")


def numOfCourse():
    while True:
        try:
            course_num = int(input("Enter number of courses: "))
            print("-------")
            return course_num
        except ValueError:
            print("Err: Invalid number.")


def findCourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Err: Invalid ID")


if __name__ == "__main__":
    students = []
    courses = []

    student_num = numOfStudent()
    print(student_num)
    for i in range(0, student_num):
        students.append(Student())
        print("-------")

    course_num = numOfCourse()
    for i in range(0, course_num):
        courses.append(Course())
        print("-------")

    print("Display students information:\n")
    for student in students:
        student.displayStudent()

    print("Display courses information:\n")
    for course in courses:
        course.displayCourse()

    x = 'y'
    while x == 'y':
        sel_course_id = input("Select a course ID: ")
        sel_course = findCourseName(courses, sel_course_id)
        print("Course name: " + sel_course + "\n")
        for student in students:
            mark = input("Enter " + student.name + "'s mark: ")
            student.set_mark(sel_course, mark)
        x = input("Do you want to select another course? y/n: ")
        print("-------")

    sel_course_id = input("Select a displayed course ID: ")
    sel_course = findCourseName(courses, sel_course_id)
    print(f"Display students' marks of course {sel_course}:\n")
    for student in students:
        student.displayMark(sel_course)
