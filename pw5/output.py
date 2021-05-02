from domain import *
from input import *
import zipfile
import os.path


menu = ["Add Student", "Add Course", "Add Mark",
        "Students List", "Courses List", "Marks List", "Sort Student By GPA",
        "Exit"]


def compression():
    with zipfile.ZipFile("student.dat", "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write("students.txt")
        my_zip.write("courses.txt")
        my_zip.write("marks.txt")


def decompression(stdscr):
    if os.path.exists("student.dat"):
        with zipfile.ZipFile("student.dat", "r") as my_zip:
            my_zip.extractall()
            with open("students.txt") as std_file:
                stdscr.addstr(std_file.read())
            with open("courses.txt") as crs_file:
                stdscr.addstr(crs_file.read())
            with open("marks.txt") as mrk_file:
                stdscr.addstr(mrk_file.read())
            stdscr.refresh()
            stdscr.getch()


def write_student_file(students):
    with open("students.txt", "w") as student_file:
        for student in students:
            student_file.write(student.get_student_info())


def write_course_file(courses):
    with open("courses.txt", "w") as course_file:
        for course in courses:
            course_file.write(course.get_course_info())


def write_mark_file(students, courses):
    with open("marks.txt", "w") as mark_file:
        for student in students:
            for course in courses:
                mark_file.write(student.get_mark(courses, course.name))


def sortByGpa(students, stdsrc):
    sorted_students = sorted(students, key=lambda student: student.gpa, reverse=True)
    for student in sorted_students:
        stdsrc.addstr(f"Student ID: {student.id}\n"
                      f"Student name: {student.name}\n"
                      f"Student DoB: {student.dob}\n"
                      f"Student GPA: {student.gpa}\n"
                      f"-------\n")


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


def system(students, courses, stdscr):
    curses.curs_set(0)

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
                stdscr.addstr(student.get_student_info())
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 4:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            stdscr.addstr(2, 0, "Display course list:\n")
            for course in courses:
                stdscr.addstr(course.get_course_info())
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row == 5:
            stdscr.clear()
            curses.echo()
            stdscr.addstr(1, 0, f"You chose {menu[current_row]}", curses.color_pair(2))
            sel_course_id = my_input(stdscr, 2, 0, "Select a course id:")
            sel_course = findCourseName(courses, sel_course_id)
            stdscr.addstr(4, 0, f"Course name: {sel_course}")
            stdscr.addstr(5, 0, f"Display students' marks:\n")
            for student in students:
                stdscr.addstr(student.get_mark(courses, sel_course))
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
