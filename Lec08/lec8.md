% Lecture 8
% Thu Jul 11, 2024

Reminders:

* Lab04 and lab05, section this afternoon
* Quiz 3 tomorrow

Today:

* LinkedList implementation
* Ordered Linked List
* Sorting algorithms

# Ordered Linked Lists

* We've discussed _unordered_ linked lists where the position of the nodes did not matter with respect to each other.
* An ordered linked list is similar to an unordered linked list except the nodes in the list are ordered with respect to each other.
* The implementation of both are similar, except we have to maintain the ordered property of the nodes when we manage the list.
    - Most methods are the same, but adding a node requires us to put a node in the correct position (instead of simply adding to the front of the list).
    - Consider two cases:
        + Adding to the front of the list

Let's implement the `add` method to see what inserting an item in the middle of the list would look like.

* Add to an ordered LinkedList

* Case 1: Add to the front

```
head [|]-->[|]-->[|]
   |  ^
   |  | (1)
(2)+->[|]
```

* Case 2: Add in the middle of the list (not-front)

```

head --> [5]-->[10]-->[15]-->[20]
               |       ^
           (2) +->[12]-+ (1)

```

# Quadratic Sorting Algorthim O(n^2)

* So far, we've discussed some ways of searching through a list:
    - Linear search: start at the beginning and check every element in the list
        * Does not require the elements to be sorted
        * O(n) complexity.
    - Binary search: check the middle, then check left or right sub lists
        * _Requires_ the elements to be sorted
        * O(log n) complexity
* But we haven't discussed how to _sort_ an unordered list.
* There are many ways to do this, and some approaches are better than others. We'll discuss several sorting algorithms and analyze their performance.

## Bubble Sort

**Idea:** Bubble sort will make several passes through the list and swap adjacent elements to ensure the largest element ends up at the end of list (assuming sort in ascending order).

```python {"id":"01J2HMABS86M8FHPY5WMZTXKHA"}
def bubbleSort(aList):
    for passnum in range(len(aList) - 1, 0, -1):
        #print("passnum ", passnum)
        for i in range(passnum):
            #print("index ", i)
            if aList[i] > aList[i + 1]:
                # swap (bubble up!)
                temp = aList[i]
                aList[i] = aList[i + 1]
                aList[i+1] = temp
            #print(aList)

list1 = [1,3,2,6,4]
bubbleSort(list1)
assert list1 == [1,2,3,4,6]

list2 = [2,2,2,2,2]
bubbleSort(list2)
assert list2 == [2,2,2,2,2]
```

## Bubble Sort Analysis

* Notice that have to make at most n-1 comparisons during the first iteration through the list.
    - Then n-2 comparisons during the 2nd iteration, etc.
* So if we count the number of comparisons in this algorithm,
    - 1 + 2 + 3 + ... + (n - 2) + (n - 1)
    - $n (n + 1) / 2$
    - So we have $O(n^2)$.
* Also note that it is $n^2$ in the BEST case scenario (the list is already sorted).
    - Each iteration does nothing, but we still compare the values anyways, performing unnecessary work.
    - In order to improve situations where the list becomes sorted during the swaps, we can check if a swap occurred during an iteration
        - If yes, continue
        - If no, then the list is sorted, so stop!
        - An implementation of this optimization in the textbook.

# Selection Sort
