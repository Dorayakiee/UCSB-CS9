% Lecture 4
% Tue Jul 2, 2024

* Quiz 1 graded.
* h00 and h01 due tonight.
* h02 and h03 released.
* Lab02 and Lab03 released.
* Holiday week student hours.

# Shallow v Deep Equality

* Python allows us to check for equality by using `==` operator for our objects.
* But Python doesn't have any knowledge of what makes a Student equal to another Student.
* So by default, Python uses the memory addresses (not the values) to determine if two objects are the same.
* This is __shallow equality__.
* Example:

```python {"id":"01J1TEM9JF79ZJZGXTBHREB0Q9"}
from Student import Student

s1 = Student("Jane", 123456)
s2 = Student("Jane", 123456)
print(s1 == s2)
s3 = s1
print(s1 == s3)
```

* In order to provide meaning of equality for two Student objects, we will have to define the `__eq__` method in our Student class.
* In this case, we can assume two Students are the same if they have the same perm number.
   - Comparing values (instead of memory addresses) is called __deep equality__.

# Operator Overloading

* We can define our own behavior for common operators in our classes
   - What does it mean for two student objects to be equal
   - Or, what does it mean to add (+) two students together
   - Python allows us to define the functionality for these operators

## Define `__str__`

* When printing our defined objects, we may get something unusual.

```python {"id":"01J1TFS2Z6QAPA20DRBZNMABTA"}
from Student import Student

s1 = Student("Gaucho", 123566)
print(s1)
```

* All objects can be printed, but Python doesn't know what to print for user-defined objects like Student.
* So it just prints the memory address (the `0x...`) of where the object exists in memory.
* In order to provide our own meaning of what Python should display when printing an object like Student, we need to define the `__str__` method.

## Overriding the `+` operator

* What would it mean to add (+) two students together?
* Maybe we can return a list collection?
* We need to define the `__add__` method.

```python {"id":"01J1TG4QJAXABEB4X8WKAZQ75H"}
from Student import Student

s1 = Student("Gaucho", 123566)
s2 = Student("Student", 999999)
x = s1 + s2
print(type(x))
for i in x:
    print(i)
```

## Overriding the `<=` and `>=` operator

* See `Student.py`

```python {"id":"01J1TGHGSJYQ86V0PK3W7V1N7D"}

from Student import Student

s1 = Student("Gaucho", 123566)
s2 = Student("Student", 999999)
print(s1 <= s2)
print(s1 >= s2)
#print(s1 > s2) # TypeError, have not defined __gt__ method
```

# Inheritance

* Let's write an `Animal` class and see what inheritance looks like:

```python
class Animal:
    # Animal class type that contains attributes for all animals

    def __init__(self, species=None, name=None):
        self.species = species
        self.name = name
    
    def setName(self, name):
        self.name = name
    
    def setSpecies(self, species):
        self.species = species

    def getAttributes(self):
        return f"Species: {self.species}, Name: {self.name}"
    
    def getSound(self):
        return "Rawr"
```

```python {"id":"01J1TH2Y2Y6E46PW1T01WVFJ0J"}
from Cow import Cow

c = Cow("Cow", "Betsy")
print(c.getAttributes())
c.setSound("Moooo")
print(c.getSound())
```

* Note that the Cow's constructor (`__init__`)  was inherited from the Animal class as well as all of its other methods.
* Because of that we didn't need to define the `getSound()` in Cow.
* But in this case, this inherited method `getSound()` may not be what we want.
* So we can redefine its functionality in the Cow class.

* In `Cow.py` we changed the `getSound()` method in the Cow class, so in this case our Cow class __overrides__ the `getSound()` method inherited from Animal.

```python {"id":"01J1THECK45CEST7QSWSDT6KC3"}
from Animal import Animal
from Cow import Cow

c = Cow("Cow", "Betsy")
print(c.getAttributes())
c.setSound("Moooo")
print(c.getSound())

a = Animal("Unicorn", "Lulu")
print(a.getAttributes())
print(a.getSound())
```

* The constructed object type will dictate which method in which is called.
* It first looks at the "constructed object type" and check if there is a method defined in that class. If so, it uses that.
* If the constructed object doesn't have a method definition in its class, then it checks the parent(s) it inherited from, and so on ...
* If there is no matching method call, then an error happens (`AttributeError`).

# Extending Superclass Methods

Some terminology:

* `Animal` in the previous example can be referred to as the Base / Parent / Super class.
* `Cow` can be referred to as the Sub / Child / Derived class.
* In the example above, we overrode the `getSound` from Animal.
* However, sometimes we only want to _extend_ the functionality, not completely replace.
    - It is possible to override methods and still use the inherited functionality by calling `super()` class methods.
    - So in this case, we override the method in the child class, but we extend the base class's functionality by using it in the child class's overwritten method.

```python {"id":"01J1TJ4C9RFHDE72RK8AP0HK9Z"}
from Cow import Cow

c = Cow("Cow", "Betsy")
c.setSound("Moooo")
print(c.getSound())

```

## Extending constructors in a Child class

* A common pattern is to redefine a subclass constructor by taking in all attributes from the parent class _and_ data specific to the subclass.

```python {"id":"01J1TJCKDXZ5A5GFQ4T58A0A84"}
from Animal import Animal
from Cow import Cow

c = Cow("Cow", "Betsy", "Moo!")
a = Animal("Unicorn", "Lulu")
zoo = [a, c]

for i in zoo:
    print(i.getAttributes())
    print(i.getSound())
    print("-------")
```

# Inheritance and Exceptions

* We can create a hierarchy of Exception types using inheritance.
    - `Exception` is the _base_ class of __all__ Exception types.
    - Remember the subclass __is a__ type of the base class.
    * This may be useful for fine-tuning certain behavior
    * For example, a network error could be because of:    
        * Malformed URL
        * Timeout
        * ...
    * Or file reading may error out due to:
        * Incorrect file name
        * Incorrect access permissions
        * ...
* Example of creating our own Exception types:

```python {"id":"01J1TJN49KNSYWRR1GDV978SEM"}
class A(Exception):
    pass

class B(A): # B inherits from A (B is an A type)
    pass

class C(Exception):
    pass

try:
    x = int(input("Enter a positive number:"))
    if x < 0:
        raise A()
except C:
    print("Exception type C caught")
except A:
    print("Exception type A caught")
except B:
    print("Exception type B caught")
except Exception:
    print("Exception of type Exception caught")

print("Resuming execution...")
```

* In the example above, B's `except` block is never called.
    - Because B __is a__ type of A (B is a child of A). So when we catch the matching type, A always matches first.

# Algorithm Analysis

* There are many ways we can try to estimate or analyze an algorithm.
* For example, we can benchmark the algorithm by calculating the time it takes for something to run.
* We can do this in Python:

```python {"id":"01J1TK50MQJRTZG8JF4JG1RH2X"}
import time

def f1(n):
    l = []
    for i in range(n):
        l.insert(0,i)
    return


def f2(n):
    l = []
    for i in range(n):
        l.append(i)
    return

print("starting f1")
start = time.time()
f1(200000)
end = time.time()
print("time elapsed: ", end - start, " seconds")

print("starting f2")
start = time.time()
f2(200000)
end = time.time()
print("time elapsed: ", end - start, " seconds")
```

* We'll get to why the time difference between adding to the list in the
  beginning and adding to the end differ in time soon enough :)
* This way of measuring algorithms has some problems like:
    * Underlying hardware (fast / slow CPU, amount of memory, disk size / speed,
      network speed, etc.)
    * How busy the computer is, how the OS is managing other programs
    * How big n is (if n is small, time is almost the same)
