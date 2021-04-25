import curses


def numOfStudent(stdscr):
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
