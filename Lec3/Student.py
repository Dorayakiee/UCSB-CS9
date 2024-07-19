class Student:
    # Student class type that contains attributes for all students
    # attributes:
    # * name
    # * perm number

    # constructor
    def __init__(self, name=None, perm=None):
        self.name = name
        self.perm = perm

    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print(f"Student name: {self.name}, perm: {self.perm}")

