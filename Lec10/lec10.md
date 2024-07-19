% Lecture 10
% Wed Jul 17, 2024

# Divide and Conquer Algorithms

* Subdivide a larger problem into smaller problems.
* Solve each smaller part.
* Combine solutions of smaller sub-problems back into the larger problem.
* We've seen this pattern with recursion where the problem can be subdivided.
* So far, we've talked about bubble sort, selection sort, and insertion sort.
    - These algorithms run in $O(n^2)$.
* But better sorting algorithms exist!
    - We can improve our run time to $O(n log n)$

# Merge Sort

**Idea:**

* Break a list into a sub lists until size == 1.
    - A sublist with 1 element is already sorted! Easy.
* Merge each small sublist together to form a sorted larger list.
* Continue to merge sublists back into the original list.

## Example

```
Initial values: 5 3 4 2 1
                 /     \
              [5 3] [4 2 1]
               /|     /   \
			  / |   [4 2] [1]
             /  |   /   \  \     Divide
-----------[5] [3] [4] [2] [1]--------------
             \ /    \  /   /     Merge
            [3 5]   [2 4] [1]
             \        \   /
              \     [1 2 4]
               \      /
			[1 2 3 4 5]

```

## Implementation

```python {"id":"01J313ETE389MD0SGAMMQT8EWP"}
def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2

        lefthalf = l[:mid]
        righthalf = l[mid:]

        # recursively, divide the left half and right half
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # merge two sorted sublists (left / right halves)
        # into the original list (l)
        i = 0 # index of lefthalf sublist
        j = 0 # index of righthalf sublist
        k = 0 # index for original list l

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                l[k] = lefthalf[i]
                i = i + 1
            else:
                l[k] = righthalf[j]
                j = j + 1
            k = k + 1
        
        # put the remaining lefthalf elements (if any) into l
        while i < len(lefthalf):
            l[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        
        # put the remaining righthalf elements (if any) into l
        while j < len(righthalf):
            l[k] = righthalf[j]
            j = j + 1
            k = k + 1

numlist1 = [9,8,7,6,5,4,3,2,1]
numlist2 = [1,2,3,4,5,6,7,8,9]
numlist3 = []
numlist4 = [1,9,2,8,3,7,4,5,6]

merge_sort(numlist1)
merge_sort(numlist2)
merge_sort(numlist3)
merge_sort(numlist4)

assert numlist1 == [1,2,3,4,5,6,7,8,9]
assert numlist2 == [1,2,3,4,5,6,7,8,9]
assert numlist3 == []
assert numlist4 == [1,2,3,4,5,6,7,8,9]
```

```python {"id":"01J31484S2Q0WJH10YHRNFJRBK"}
# with some print statements for debugging
def merge_sort(l):
    print('Merge:', l)
    if len(l) > 1:
        mid = len(l) // 2

        lefthalf = l[:mid]
        righthalf = l[mid:]

        # recursively, divide the left half and right half
        merge_sort(lefthalf)
        merge_sort(righthalf)

        # merge two sorted sublists (left / right halves)
        # into the original list (l)
        i = 0 # index of lefthalf sublist
        j = 0 # index of righthalf sublist
        k = 0 # index for original list l

        print('Start merge phase!')
        print('original list', l, 'lefhalf', lefthalf, 'righthalf', righthalf)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                l[k] = lefthalf[i]
                i = i + 1
            else:
                l[k] = righthalf[j]
                j = j + 1
            k = k + 1
        
        # put the remaining lefthalf elements (if any) into l
        while i < len(lefthalf):
            l[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        
        # put the remaining righthalf elements (if any) into l
        while j < len(righthalf):
            l[k] = righthalf[j]
            j = j + 1
            k = k + 1
        print('sorted original list', l, '\n')

l = [5,3,4,2,1]
merge_sort(l)
```

## Merge Sort Analysis

```
Merge sort breaks the list into two equal parts recursively.

size 8      [1 2 3 4 | 5 6 7 8]    <-- 0
                 /     \
height 3    [1 2 3 4] [5 6 7 8]    <-- 1
             /    \      /   \ 
          [1 2] [3 4] [5 6] [7 8]  <-- 2
           / \   / \   / \   / \
          1  2   3  4  5  6  7  8  <-- 3

* Height (balanced tree) => log_2 n

* For each level, the merge operation compares n elements.
 => n * log n => O(n log n)
  merge  #of levels     best and worst case!
```

* Height (of the tree) = $log_2 n$.
* For each level, the merge operation compares n elements.
* $n * log n$ --> $O(n log n)$
    - $log n$ is the number of levels we break the list into.
    - $n$ is the number of comparisons for each merge operation.

* Merge Sort breaks the list into two equal parts per recursive iteration.
* Note that the height (the number of levels) of the tree $log n$ (for 8 nodes, we have a height of 3).
* For each level, the merge step needs to compare $n$ elements.
    - So if there are $log n$ levels and we need to do $n$ comparisons to merge the elements for each level, then we have $O(n log n)$ running time.
* One disadvantage of Merge Sort is it requires O(n) additional space when creating the left and right sublists.
    - Can be problematic if the list we're trying to sort is very large.

# Quicksort

* Another divide-and-conquer sorting algorithm.
* Can improve running times to $O(n log n)$ in a typical case.

**Idea:** 

* We can sort a list by subdividing the list based on a _pivot_ value
    - Place elements < pivot to the left-side of the list
    - Place element > pivot to right-side of the list
    - Recurse for each left / right portion of the list
    - When sub list sizes == 1, then the list is sorted
