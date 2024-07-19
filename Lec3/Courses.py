# Courses.py

# from [filename (without .py)] import [name]
from Student import Student

class Courses:
    '''
    Class representing a collection of courses.
    Courses are organized by a dict where the key is
    the course number and the value is a list of Students
    in the course.
    '''

    def __init__(self):
        self.courses = dict()

    def getCourses(self):
        return self.courses

    def addStudent(self, student, courseNum):
        # first, check if course exists or not
        if self.courses.get(courseNum) == None:
            self.courses[courseNum] = [student]
        else:
            self.courses[courseNum].append(student)
    
    def printCourses(self):
        for courseNum in self.courses:
            print("CourseNum: ", courseNum)
            for student in self.courses[courseNum]:
                student.printAttributes()
            print("---")

s1 = Student("Student Gaucho", 123456)
UCSB = Courses()
UCSB.addStudent(s1, "CS9")
UCSB.printCourses()

courses = UCSB.getCourses()
assert courses == {"CS9": [s1]}

s2 = Student("Jane Namerson", 123456)
UCSB.addStudent(s2, "CS9")
UCSB.addStudent(s2, "CS19")
UCSB.printCourses()