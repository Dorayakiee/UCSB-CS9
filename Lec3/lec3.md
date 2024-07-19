% Lecture 3
% Thu Jun 27, 2024

* Lab00 and Lab01 released.
* Quiz 1 will be available tomorrow: 1 question, 2 parts.

# Catching Multiple Exceptions

Let's modify our code so another type of exception (`ZeroDivisionError`) may be caught.

```python {"id":"01J1DK60J45QTZ3DGNSNK0BJ5G"}
while True:
    try:
        x = int(input("Enter an int: "))
        print(x/0)
        break
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception:
        print("Input was not an int type")
    print("Try again...")
print(x)
```

* In this case, the programs will either complain that a number type was not entered, or if it was entered, we'll get a `ZeroDivisionError`.
    - The program in this case will never execute "correctly" (without throwing an error, or even exiting the loop)
* But the important thing here is that we can catch multiple exception types
* The rule is:
    - `except` statements are check top-down
    - The first matching exception type will be executed
    - Then the program jumps past ALL the other except blocks and code execution resumes

## Example of functions raising exceptions

```python {"id":"01J1DKN6FR61NY6SP42C6ZMG42"}
def divide(nu, de):
    if de == 0:
        raise ZeroDivisionError()
    return nu / de

try:
    print(divide(1,1))
    print(divide(1,0))
    print(divide(2,2)) # note this doesn't get executed
except ZeroDivisionError:
    print("Error: cannot divide by zero")

print("Resuming execution...")

```


* In this scenario, we have an exception raised in the divide function
* Since there isn't an except statement in `divide()`, the exception message gets passed to the calling function
    - Since divide was called in a  `try` block, then we check the except statements for the first match
    - If a match exists, then the first `except` block is executed, and execution resumes
* If an exception is raised and we *never* handle it in an except block, then the program will crash with an error message.

# Python Objects and Classes

* Objects are a way for programmers to define their own Python data types and create "abstractions"
* Each object may have ceratain state that gets modified through program execution
* Object-oriented programming (OOP) is the way programs use and modify objects to solve problems and model data
* OO programming is not *required*
    - It's more of a way to organize, read, and maintain software we write
* We have been using objects already, for example:

```python {"id":"01J1DMARJ2C57MYKQ5G2NDZ355"}
x = [1,2,3]
print(type(x))
print(x.count(3))
print(x.count(-1))
x.append(0)
print(x)
```

* `count`, `append`, etc. are all example of **methods** that can be called on a object
* **Methods** are like functions but they are associate with an object
* In this case, Python already defined its own  class `list` that we can use, but sometimes we want to create our own specific objects for the applications we're trying to build!

## Student class example

```python {"id":"01J1DMH0SZN4WAVXQ28QCN58EH"}
class Student:
    # Student class type that contains attributes for all students
    # attributes:
    # * name
    # * perm number
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print(f"Student name: {self.name}, perm: {self.perm}")

s = Student()
s.setName("Chris Gaucho")
s.setPerm(123123123)
s.printAttributes()
```

* When defining methods, the `self` parameter represents the current object we're calling the method on.
* In the example above, `s` is the variable storing the created Student object.
* When we define these methods, the first parameter (`self`) is the *instance* of the object `s`
* We can then use and manipulate the state of the object with these methods using the `self` parameter.

## Default Constructor

* We can provide either default values or set values of the object when creating it through the parameter list
* In the example above, we can set an empty object without any initial attributes, which may cause an error when trying to use them
* The constructor will set `self.name` and `self.perm` to the `None` value

```python {"id":"01J1DNC27A8G3SSHGWPANTDCR4"}
class Student:
    # Student class type that contains attributes for all students
    # attributes:
    # * name
    # * perm number

    # default constructor
    def __init__(self):
        self.name = None
        self.perm = None

    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print(f"Student name: {self.name}, perm: {self.perm}")

s = Student()
s.printAttributes()
s.setName("Chris Gaucho")
s.setPerm(123123123)
s.printAttributes()

```

## Overloading constructor

```python {"id":"01J1DNH31F15WXG2XR658W00RV"}
class Student:
    # Student class type that contains attributes for all students
    # attributes:
    # * name
    # * perm number

    # constructor
    def __init__(self, name, perm):
        self.name = name
        self.perm = perm

    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print(f"Student name: {self.name}, perm: {self.perm}")

s = Student("Jane Namerson", 999111000)
s.printAttributes()

```

## Initializing default values in the constructor

```python {"id":"01J1DNNAXZ7GKDPMBGC1JGJARP"}
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

s = Student("Jane Namerson", 999111000)
s.printAttributes()
t = Student()
t.printAttributes()
r = Student(perm=101010)
r.printAttributes()

```

* In this case, we can pass in parameters or not. If not, then `None` will automatically be assigned to `self.name` and `self.perm`

## Example of using objects in code

```python {"id":"01J1DNYSZK0BYZ5RJ0BCR80ZS7"}
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

s1 = Student("Jane Namerson", 999111000)
s2 = Student("Mark Nominal", 123123123)
s3 = Student("Dewey Names", 101010)

studentList = [s1, s2, s3]

for s in studentList:
    s.printAttributes()

# Using `assert` statements to test correct functionality
t = Student()
assert t.name == None
assert t.perm == None

r = Student("gaucho", 8675309)
assert r.name == "gaucho"
assert r.perm == 8675309

```

# Container classes

* Let's continue to expand on our Student class
* Classes are also useful to organize/maintain state of a program
* Student objects are useful to organize the attributes of a *single* student
* But let's imagine we are trying to write a database of lots of students
    - The database may be useful to search for students based on attributes
    - We will need to add / remove students from the database
    - We can define a class to represent a collection of courses containing students
    - Let's set up a collection of courses such that a dictionary key is defined by the course number and the value is a list of student objects.
* Continued in `Courses.py`


```python
print("Hello!")
```

