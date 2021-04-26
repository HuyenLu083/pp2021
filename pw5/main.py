from output import *
import curses


def main(stdscr):
    students = []
    courses = []
    system(students, courses, stdscr)
    write_student_file(students)
    write_course_file(courses)
    compression()
    decompression(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)
