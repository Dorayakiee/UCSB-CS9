% Lecture 5
% Wed Jul 3, 2024

* Quiz 2 released after class today, 1:50 PM.
  Available to take until Friday 11:59 PM.

# Algorithm Analysis

* There are many ways we can try to estimate or analyze an algorithm.
* For example, we can benchmark the algorithm by calculating the time it takes for something to run.
* We can do this in Python:

```python {"id":"01J1X0MA1SR1A34QD800D272RJ"}
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

# Asymptotic Behavior

* We want to analyze approximately how fast an algorithm runs when the size of the input approaches infinity.
* So instead of calculating the raw time of how fast the algorithm runs on our computers, we can approximate the number of instructions the algorithm will take with respect to the size of the input.
   - Steps/instructions can include things like assigning values to variables, evaluating expressions, arithmetic operations, loop iterations, etc.

* A simple example:

```python
for i in range(10):
   print(i)
```

* Counting expressions in this case;
   - Assignments: `i = 0`, `i = 1`, `i = 2`, ... (10 steps)
   - `print()`: (10 steps)
   - Algorithm takes 20 steps.
* The algorithm runs in __constant time__, since there isn't a variable input and will always take the same number of instructions to run.
* Let's change our code taking in a variable input size:

```python
def foo(n):
   for i in range(n):
      print(i)
```

* Now the number of instructions in this algorithm is dependent on the value of $n$.
* So let's try to express the number of instructions as a polynomial with to $n$,
   - We can denote the number of instructions with respect to $n$ as $T(n)$.
* T(n) = n assignment statements + n print statements
       = 2n

## Order of magnitude function (Big-O)

* Since we have no idea how large $n$ will be, we want to assume the __worst-case__ scenario when analyzing our algorithms
   - And in this case, the worst-case scenario is when $n$ approaches infinity.
* Since $n$ approaches infinity, we can ignore lower order terms and coefficients
   - Does the 3 really matter when we have 1,000,000,000 + 3
    * See:
      <http://science.slc.edu/~jmarshall/courses/2002/spring/cs50/BigO/index.html>
      for an example of how lower-order terms converge when $n$ approaches
      infinity
* So we can express the above algorithm by dropping all lower order terms, constants, and coefficients, T(n) = 2n  ---> O(n)
* Note: Constant-time algorithms are denoted as O(1).

```python
def bar(n):
   x = 0
   for i in range(n):
      for j in range(n):
         x = i + j
```

* `x = 0` is 1 instruction.
* `i` assignment statements (n instructions)
* `j` assignment statements ($n^2$ instructions)
* `i + j` arithmetic expression ($n^2$ instructions)
* `x` reassignment statements ($n^2$ instructions)
   - $T(n) = 1 + 3n^2 + n$
* Drop all lower-order terms, coefficients, and constants to get
   - $O(n^2)$
   
```python
def baz(n):
   for i in range(n):
      return i
```

* Note that in this example, `i` gets assigned to 0.
* But then `i` is immediately returned before reassigning `i` to 1. Only executes the first iteration no matter what `n` is.
* So this algorithm is O(1) (constant-time).

# Recursion

* Recursion is when a function contains a call to itself.
* Recursive solutions are useful when the result is dependent on the result of sub-part of the problem.

## The three laws of recursions

1. A recursive algorithm must have a _base case_.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself.

In general, recursive algorithms must use the solution of sub-parts of the problem to solve a general problem.

## Common Example: Factorial 

* $N! = N * (N - 1) * (N - 2) * ... * 3 * 2 * 1$
* $N! = N * (N - 1)!$
* We can solve $N!$ by solving the $(N - 1)!$ sub-part
* Base case: 0! == 1

```python {"id":"01J1X3DRQ7HEW76X16QEW8VPWQ"}
def factorial(n):
    if n == 0:   # base case
        return 1
    return n * factorial(n - 1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(8))
```

## Function Calls and the Stack

* The Stack is a data structure with a Last In, First Out (LIFO) property.
* We can only access the elements at the top of the stack.
* We won't go through an implementation yet, but we can conceptualize this at a high level
* Function calls utilize a stack ("call stack"), and organize how functions are called, and how expressions that call functions wait for the functions' return values.
    - When a function is called, you can think of that function state being added (or "pushed") on the stack.
    - When a function finishes execution, it gets removed (or "popped"), from the stack
    - The top of the stack is the function that is currently running

```python
def double(n):
    return 2 * n

def triple(n):
    return n + double(n)

print(triple(5))
```

```
double(5)         --> 10
triple(5)         --> 5 + double(5) = 5 + 10 = 15
print(triple(5))  --> 15
```

* Going back to our recursive factorial example, let's trace `factorial(3)`

```
factorial(0) --> 1
factorial(1) --> 1 * factorial(0) = 1 * 1 = 1
factorial(2) --> 2 * factorial(1) = 2 * 1 = 2
factorial(3) --> 3 * factorial(2) = 3 * 2 = 6
```

## Common example: Fibonacci Sequence 

* A fibonacci sequence is the n-th number in the sequence that is the sum of the previous two
    - $f(n) = f(n-1) + f(n-2)$
* $f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, ...$

```python {"id":"01J1X4GGMYVAYECR823XDV15J7"}
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    #if n < 2:  # another way to write the base
    #    return n

    return fib(n - 1) + fib(n - 2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))
```

* Evaluate `fib(4)` by hand

```
fib(4)
fib(3)                    +  fib(2)
fib(2)          + fib(1)  +  fib(2)
fib(1) + fib(0) + fib(1)  +  fib(2)
1      + fib(0) + fib(1)  +  fib(2)
1      + 0      + fib(1)  +  fib(2)
1      + 0      + 1       +  fib(2)
1      + 0      + 1       +  fib(1) + fib(0)
1      + 0      + 1       +  1      + fib(0)
1      + 0      + 1       +  1      + 0
3
```

# Testing 

## Complete Test

* Complete test: Testing every possible path through our code in possible situation (input values)
    - Generally infeasible
    - Imagine a simple program that takes in 4 integers and prints out the max
        - In python3, the range of valid integers is a lot!
        - Limited to memory (unlike other languages like C++ / Java where an int
          type is stored in 32 bits (4 bytes)
        - The number of computations to test EVERY POSSIBLE combination of the 4
          integers will take A LONG TIME to compute!
* __Unit testing__: Testing individual pieces (units) of a program to ensure behavior.

## Test Driven Development (TDD)

1. Write test cases that describe what the intended behavior of a unit of
   software should. Kinda like the requirements of your piece of software
2. Implement the details of the functionality with the intention of passing the
   tests
3. Repeat until the tests pass.

* Imagine large software products where dozens of engineers are trying to add
  new features / implement optimizations all at the same time
* Having a "suite" of tests before deploying software to the public is essential
    * Someone may modify changes that work for a current version, but breaks
      functionality in a future version
    * Rigorous tests enable confidence in the stability in software

