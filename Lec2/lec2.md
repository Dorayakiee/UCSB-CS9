% Lecture 2
% Wed Jun 26, 2024

# Functions

```python {"id":"01J1B0D368GZF4XATA8DB9BSR3"}
def double(n):
    # Returns 2 times the input parameter `n`
    return 2 * n

print(double(3))
```

* Note: A function does not have to return anything.
* If a function doesn't have a specific return value, it returns a special `None` type.

```python {"id":"01J1B0QHPHR154P1CK4998N89D"}
def double_print(n):
    # Returns 2 times the input parameter `n`
    print(2 * n)

double_print(3)
print(type(double_print(3)))
```

# Mutable vs Immutable

* Why should we care about immutable vs mutable properties?
    - Depending on whether something is mutable/immuatable, it affects how the data is treated when passing it in a function.
* When immutable types are passed into a function, a **copy** of that variable is made and used within the function.
    - Once the function returns, the immutable value does not change!
* When mutable types are passed into a function, the parameter is used within the function (no copy is made).
    - Once the function returns, the mutable value does change!

```python {"id":"01J1B119GGF8F7XC5T0KSS9X3V"}
def changeList(x):
    x[0] = "!"
    return x

a = ["C", "S", "9"]
print("a before changeList:", a)
print(changeList(a))
print("a after changeList:", a)

def changeString(x):
    x = x.replace("C", "!")
    return x

print("")

b = "CS 9"
print("b before changeString:", b)
print(changeString(b))
print("b after changeString:", b)
```

# Control Structures

## if statements

```
if BOOLEAN_EXPRESSION:
  STATEMENT ...
```

* If `BOOLEAN_EXPRESSION` is True, then execute statements. If False, skip the statements.

## if/else statements

```
if BOOLEAN_EXPRESSION:
  STATEMENT #1
else:
  STATEMENT #2
```

* If BOOLEAN_EXPRESSION is True, then execute statement #1.
* If BOOLEAN_EXPRESSION is False, then execute statement #2.

## elif statements

```python {"id":"01J1B1PHM11HY54YKVPW2R8XHS"}
x = True
if x:
    print("Shouldn't print")
elif 4 < 5:
    print("4 < 5, of course!")
else:
    print("Shouldn't print")
```

## While loops

```
while BOOLEAN_EXPRESSION:
    STATEMENTS
```

* if BOOLEAN_EXPRESSION is True, execute STATEMENTS in the body of the loop.
* If BOOLEAN_EXPRESSION is False, exit the loop.

```python {"id":"01J1B1TF6Y8NBP0SCM9P6PPWRD"}
# will always execute since the condition is always True
while True:
    print("wooooo!")
```

## For loops

```
for VARIABLE in COLLECTION:
    STATEMENTS
```

* Common pattern in Python loops.
* `range()` is a function used for looping if we know the number of iterations we need.
    - `range(x)` returns a collection of numbers from 0 up to (but not including) `x`
    - `range(x, y)` returns a collection of numbers from `x` up to (but not including) `y`

```python {"id":"01J1B22RPG94N6M1HNC0TXGTYX"}
for x in range(4):
    print(x, "Hi!" * x)
    print("------")
```

```python {"id":"01J1B26VEXNGQERA6YSSJRYMH5"}
for x in range(2,4):
    print(x, "Hi!" * x)
    print("------")

```

# Sets

* Like a mathematical set
* A collection of items with:
    - No duplicates
    - Order and position does not matter

```python {"id":"01J1B2C0Q7XR6PSS5QBQC1VYDB"}
s = set([2,4,6])
print(s)
print(type(s))
print(3 in s)
print(5 not in s)
print(len(s))

# combine values from two sets
t = {4,5,6} # another way of creating a set
combined_set = s | t
print(combined_set)

# Get the common elements from two sets
intersecting_set = s & t 
print(intersecting_set)
```

# Dictionaries

* Otherwise known as "tables" or "maps".
    - A unique "key" mapping to a "value".
* Gives more precise indexing than lists.

```
DICT = { key1 : value1, key2 : value2, ...  }
```

```python {"id":"01J1B2SCXMP8CRKEQGD9G6XQJ5"}
D = dict()
print(D)
print(len(D))
print(type(D))

D = { 'Alex': 19, 'David':20, 'Jane': 20 }
print(D)
print(len(D))
print("David's age is: ", D["David"])

for x in D:
    print(x) # prints the key
    print(D[x]) # prints the value

```

## Restrictions on using Dictionaries

* Keys must be an immutable type
    - int, strings, tuples, but **not** lists
* Values can be any type (immutable or mutable), and do not have to be unique.

```python {"id":"01J1B34YKREZS0QWPN00FCBFAP"}
D = { 'Alex': 19, 'David':20, 'Jane': 20 }
value = D.pop("David")
print(value)
print(D)

# print(D["asdfasdf"]) # will fail
value = D.get("asdfasdf")
if value == None:
    print("Key not found!")

D["No One"] = 0 # adds new key to D
print(D)
D["Jane"] = 21 # updates key already in D
print(D)
```

# Python Errors

* We've seen before Python complains before even running the program:

```python {"id":"01J1B3JEJAHHPBSE5SXGRB9QST"}
print("Start")

PYTHON!

print( End )
```

* In this case, the program did not run at all. "Start" never printed.
* Before anything happened, Python is telling us that `PYTHON!` is a syntax error.
* Before any Python script runs, it gets parse the file and performs a simple check to make sure all expressions are legal.
* If not, it will print a syntax error.
* Let's remove the offending line:

```python {"id":"01J1B3QV68BTDKZ243NZSZWBXA"}
print("Start")

print( End )

```

* We get another type of error that happens *while* the code is running.
* Errors that happen during program execution are called "runtime errors".

# Exceptions

* Exceptions are errors that occur during program execution.
* So far, when we've encountered runtime errors, the program crashes.
* However, there are ways to recover from runtime errors by handling exceptions in our code.
* In the above code, it's complaining about a certain type of error called `NameError`.
* There are many types of exception types that can occur during runtime.
* For example:

```python {"id":"01J1B40D07X5HMTYS08E904B5R"}
print("Start!")
print(1 / 0)
```

* Gives us the exception `ZeroDivisionError`

```python {"id":"01J1B42BB42N3NRGA5PN9Y1BM2"}
print("Start!")
print('5' + 5)
```

* This returns a `TypeError`. Python `+` cannot handle a string with an int type.

## Handling Exceptions

The general rule of exception handling is:

* If an exception is raised in a program and nobody catches the exception, the program will crash.
* But we can handle exceptions with a general structure called a `try / catch`.

```python {"id":"01J1B48AFGJRJDGMY5TM55GW33"}
while True:
    try:
        x = int(input("enter an int: "))
        break
    except Exception:
        print("Input was not a number type")
    print("Let's try again...")
print(x)
```

The flow of exception is:

* Everything within a `try` block executes normally.
* If an exception occurs in the `try` block, execution halts and an exception is passed to the corresponding `except` block.
* The `except` block tries to catch a certain exception type
    - Note that `Exception` catches all types of exceptions
      (`NameError`, `TypeError`, `ZeroDivisionError`, `ValueError`)
* If there is a matching type in the `except` statement, then the first matching `except` block will execute.
* Once done, program execution resumes past the `except` block(s).
* If no exceptions were caught, then the program will terminate with an error message.
