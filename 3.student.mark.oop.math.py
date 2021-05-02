import math
import numpy as np
import curses

menu = ["Add Student", "Add Course", "Add Mark",
        "Students List", "Courses List", "Marks List", "Sort Student By GPA",
        "Exit"]


class Student:
    def __init__(self, __id, __name, __dob):
        self.id = __id
        self.name = __name
        self.dob = __dob
        self.gpa = 0
        self.marks = np.array([[], [], []])

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.marks

    def set_id(self, __id):
        self.id = __id

    def set_name(self, __name):
        self.name = __name

    def set_dob(self, __dob):
        self.dob = __dob

    def set_mark(self, __course, __mark, __credit):
        self.marks = np.append(self.marks, [[__course], [__mark], [__credit]], axis=1)

    def get_gpa(self, courses):
        sum_credits = 0
        for i in range(len(courses)):
            self.gpa += int(self.marks[1][i]) * int(self.marks[2][i])
            sum_credits += int(self.marks[2][i])

        self.gpa = math.floor((self.gpa / sum_credits) * 10) / 10
        return self.gpa

    def display_mark(self, stdscr, courses, course):
        for i in range(len(courses)):
            if len(self.marks[0]) > i:
                if self.marks[0][i] == course:
                    stdscr.addstr(f"{self.name} 's mark: {self.marks[1][i]}\n")
                    break
            else:
                stdscr.addstr(f"{self.name} 's mark: none\n")
                break

    def display_student(self, stdsrc):
        stdsrc.addstr(f"Student ID: {self.id}\n"
                      f"Student name: {self.name}\n"
                      f"Student DoB: {self.dob}\n"
                      f"Student GPA: {self.gpa}\n"
                      f"-------\n")


class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_credit(self, credit):
        self.credit = credit

    def display_course(self, stdsrc):
        stdsrc.addstr(f"Course ID: {self.id}\n"
                      f"Course name: {self.name}\n"
                      f"Course credit: {self.credit}\n"
                      f"-------\n")


def my_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    __input = stdscr.getstr(r + 1, c, 20).decode('utf-8')
    return __input


def findCourseName(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_name()
    print("Err: Invalid ID")


def findCourseCredit(courses, course_id):
    for course in courses:
        if course.get_id() == course_id:
            return course.get_credit()
    print("Err: Invalid ID")


def sortByGpa(students, stdsrc):
    sorted_students = sorted(students, key=lambda student: student.gpa, reverse=True)
    for student in sorted_students:
        student.display_student(stdsrc)


def print_menu(stdscr, current_row):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == current_row:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    students = []
    courses = []

    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    current_row = 0
    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 0:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            std_id = my_input(stdscr, 2, 0, "Enter student ID:")
            std_name = my_input(stdscr, 4, 0, "Enter student name:")
            std_dob = my_input(stdscr, 6, 0, "Enter student date of birth:")
            students.append(Student(std_id, std_name, std_dob))
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 1:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            course_id = my_input(stdscr, 2, 0, "Enter course ID:")
            course_name = my_input(stdscr, 4, 0, "Enter course name:")
            course_credit = my_input(stdscr, 6, 0, "Enter course credit:")
            courses.append(Course(course_id, course_name, course_credit))
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 2:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            sel_course_id = my_input(stdscr, 2, 0, "Select a course id:")
            sel_course = findCourseName(courses, sel_course_id)
            sel_credit = findCourseCredit(courses, sel_course_id)
            stdscr.addstr(4, 0, f"Course name: {sel_course}")
            for i, student in enumerate(students):
                mark = my_input(stdscr, 5 + 2*i, 0, f"Enter {student.name}'s mark:")
                student.set_mark(sel_course, mark, sel_credit)
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 3:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            stdscr.addstr(2, 0, "Display student list:\n")
            for student in students:
                student.display_student(stdscr)
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 4:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            stdscr.addstr(2, 0, "Display course list:\n")
            for course in courses:
                course.display_course(stdscr)
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 5:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            sel_course_id = my_input(stdscr, 2, 0, "Select a course id:")
            sel_course = findCourseName(courses, sel_course_id)
            stdscr.addstr(4, 0, f"Course name: {sel_course}")
            stdscr.addstr(5, 0, f"Display students' marks of course {sel_course}:\n")
            for student in students:
                student.display_mark(stdscr, courses, sel_course)
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 6:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            for student in students:
                student.get_gpa(courses)
            stdscr.addstr(2, 0, "Display student list by GPA descending:\n")
            sortByGpa(students, stdscr)
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 7:
            break

        print_menu(stdscr, current_row)
        stdscr.refresh()


curses.wrapper(main)
