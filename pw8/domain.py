import numpy as np
import math


# class BackgroundThread(threading.Thread):
#     def __init__(self, students, courses, sleepTime):
#         threading.Thread.__init__(self)
#         self.__students = students
#         self.__courses = courses
#         self.__sleepTime = sleepTime
#
#     def run(self):
#         with open("students.pkl", "wb") as infile:
#             pickle.dump(self.__students, infile)
#             pickle.dump(self.__courses, infile)


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

    def get_mark(self, courses, course):
        for i in range(len(courses)):
            if len(self.marks[0]) > i:
                if self.marks[0][i] == course:
                    return f"{self.name}'s mark for course {course}: {self.marks[1][i]}\n"
                    break
            else:
                return f"{self.name}'s mark: none\n"
                break

    def get_student_info(self):
        return (f"Student ID: {self.id}\n"
                f"Student name: {self.name}\n"
                f"Student DoB: {self.dob}\n"
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

    def get_course_info(self):
        return (f"Course ID: {self.id}\n"
                f"Course name: {self.name}\n"
                f"Course credit: {self.credit}\n"
                f"-------\n")