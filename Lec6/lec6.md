% Lecture 6
% Tue Jul 9, 2024

* h00 graded
* h02 and h03 due tonight
* h04 and h05, Lab04 and Lab05 released

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

# Pytest

* Pytest is a framework that allows developers to write tests to check the correctness of their code.
* Gradescope actually uses pytest to check the "correct" answer with students' submissions.
* We can write functions that start with `test_`, and the body of the function can contain `assert` statements.
   - Pytest will run each of these functions and report which tests passed/failed.
* Try and install Pytest on your computer (will use this in our examples)
  Installation Guide: <https://docs.pytest.org/en/stable/getting-started.html>
* Windows Installation Guide (created by previous Learning Assistants): [Python
  and Pytest Installation Guide for
  Windows](https://drive.google.com/file/d/1nPCwIA8cBAkiJ-kOKZFjkOskD94jmWYn/view)

## Example

* Write a function `biggestInt(a,b,c,d)` that takes 4 int values and returns the largest.
* Let's write our tests first! (TDD)
* See `test.py` in lecture 6 code.

Command to run pytest on `test.py`:

* Navigate to the folder containing `test.py`
* (On mac terminal): `python3 -m pytest test.py`
    * Note: may need to replace `python3` with `python` on Windows.


# Python Lists vs Python Dictionaries

* Let's observe the performance between lists and dictionaries.
* The following program counts the number of words in a file using a list and
  using a dictionary.
    - They do the same thing, but the performance is much different...
    - `wordlist.txt` : File containing a collection of words, one per line.
        - <https://ucsb-cs8.github.io/m19-wang/lab/lab07/wordlist.txt>
    - `PeterPan.txt` : You can download classic novels from the Gutenberg
      Project as a .txt file!
        - <https://www.gutenberg.org/ebooks/16>

* See `wordcount.py`.
* Python lists are efficient if we know the _index_ of the item we're looking for.
   - The reason why adding to the front of the list is slow is because lists have to "make room" for the element to be at index 0.
      - All existing elements of the list need to shift one index up in the order for the inserted element to be placed at index 0.
   - Adding to the end of the list is not nearly as expensive because no shifting occurs.
* For this example, since we are looking for the value in the list (without knowing the index), we are searching through the _entire_ WORDLIST for every word in `peter-pan.txt`.
* Python dictionaries are efficient when looking up a key value.
   - Dictionary values are actually stored in an underlying list.
   - Keys are converted into a numerical value, which is passed into a "hash function".
      * The purpose of the hash function is to output the index for the underlying list based on the key value.
      * We do not have to scan the underlying list structure since a key will always be placed into a specific location in the underlying list.
      * We won't go into the implementation now, but we'll revisit in more detail later.
* There are many ways to solve a problem in programming. But understanding how certain tools work and choosing the right data structures/algorithms is important!

__Recall:__

* Recall our benchmarking algorithm when inserting elements to the front of a list:

```python
def f1(n):
   l = []
   for i in range(n):
      l.insert(0, i)
   return l
```

* Since we're inserting elements at the front of the list, we need to move the existing elements over by one in order to make room for them.
   - So the 1st iteration takes one step. (easy)
   - The 2nd insertion needs to move the first element to make, and then insert the element.
   - The 3rd insertion needs to the first _and_ the second element over and so on ...
* We can say the number of steps this loop has:
   - $1 + 2 + 3 + ... + n$
   - And this simplifies to $n (n - 1) / 2$
   - `f1` is $O(n^2)$

# Binary Search Algorithm

* Binary search is a useful algorithm to search for an item in a collection _if the items are already sorted_.
* Since the collection is already sorted, we can check the middle to see if the item we're looking for is there.
   - If the middle element is the one we're looking for, we're done!
   - If the item we're looking for is < the middle element, then we don't have to search the right side of the collection.
   - If the item we're looking is > the middle element, then we don't have to search the left side of the collection.
* Since each comparison is eliminating _half_ of the search space, this algorithm has a logarithmic property.
   - Algorithm performs in $O(log n)$ time.   

See `binarysearch.py`.
