students = []
courses = []
marks = []

def numOfStudent():
    std_num = int(input("Enter number of student in the class: "))
    return std_num


def studentInfo():
    std_id = input("Enter student ID: ")
    std_name = input("Enter student name: ")
    std_dob = input("Enter student date of birth: ")
    return std_id, std_name, std_dob


def numOfCourse():
    course_num = int(input("Enter number of courses: "))
    return course_num


def courseInfo():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return course_id, course_name


def studentMarks(students, course, marks):
    for i in range(len(students)):
        marks.append({course: {}})
        mark = float(input("Enter " + students[i].get("name") + "'s mark \n"))
        marks[i].update({course: mark})

        
def displayCourses():
    print("Course information: \n")
    for i in range(len(courses)):
        print("Course ID: " + courses[i].get("id") + "\n")
        print("Course name: " + courses[i].get("name") + "\n")

        
def displayStudents():
    print("Student information: \n")
    for i in range(len(students)):
        print("Student ID: " + students[i].get("id") + "\n")
        print("Student name: " + students[i].get("name") + "\n")
        print("Student DoB: " + students[i].get("dob") + "\n")

        
def displayMarks():
    print("Student marks for this course\n")
    for i in range(len(students)):
        print(students[i].get("name") + "'s mark' " + ":")
        print(marks[i])
        print("\n")


if __name__ == "__main__":
    student_num = numOfStudent()
    print(student_num)
    for i in range(0, student_num):
        std_id, std_name, std_dob = studentInfo()
        students.append({"id": std_id, "name": std_name, "dob": std_dob})

    course_num = numOfCourse()
    for i in range(0, course_num):
        course_id, course_name = courseInfo()
        courses.append({"id": course_id, "name": course_name})

    x = 'y'
    while x == 'y':
        sel_course_id = input("Select a course ID: ")
        for i in range(len(courses)):
            if courses[i].get("id") == sel_course_id:
                print("course name: " + courses[i].get("name") + "\n")
                studentMarks(students, courses[i].get("name"), marks)
        x = input("Do you want to select another course? y/n: ")

    displayStudents()
    displayCourses()
    displayMarks()
