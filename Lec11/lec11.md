% Lecture 11
% Thu Jul 18, 2024

# Quicksort

* Another divide-and-conquer algorithm
* Can improve running times to **O(n log n)** in a typical case, but we'll see how this can also lead to $O(n^2)$ in a worst-case scenario

**Idea:**

* We can sort a list by subdividing the list based on a _pivot_ value
    * Place elements < pivot to the left-side of the list
    * Place elements > pivot right-side of the list
    * Recurse for each left / right portion of the list
    * When sub list sizes == 1, then entire list is sorted

```
       [ (< pivot)   pivot   (> pivot) ]
        /                         \
[(< pivot') pivot' (> pivot')]    [(< pivot'') pivot'' (> pivot'')]
    ...                                 ...
```

## How do we partition the list into left/right sub-lists?

1. Choose pivot (typically first element in the list).
2. "Left mark" index is on the left-most side of the list,
   "right mark" index is on the right-most side of the list.
   And both leftmark and rightmark work inwards.
3. Find an element in the left side (using leftmark index) that's out-of-place (> pivot).
4. Find an element in the right side (using rightmark index) that's out-of-place (< pivot).
5. Swap out-of-place elements with each other.
6. Continue doing steps 2--5 until the rightmark index < leftmark index.
7. Swap the pivot with rightmark index.
  - We're putting the pivot element in the correct place!

## Quick Sort Hand Drawn Example

- `P` = Pivot, `L` = Left iterator, `R` = Right iterator

```
Initial values: 7 9 0 1 8

P L     R
7 9 0 1 8
  L > P? Stop L
  R < P? No, R-1

P L   R
7 9 0 1 8
  R < P? Stop R
  Both stopped, swap L and R

P L   R
7 1 0 9 8
    L+1

P   L R
7 1 0 9 8
    R-1

P   RL
7 1 0 9 8
  R < P? Stop R
  L > P? No, L+1

P   R L
7 1 0 9 8
  R < P? Stop R
  L > P? No, L+1

if L >= R, stop, swap P and R

0 1 7 9 8

Subdivide array based on new pivot:

0 1 | 7 | 9 8

P LR
0 1


P LR
9 8

P R L
9 8

if L >= R, stop, swap P and R

=> 0 1 7 8 9

```

## Implementation

```python {"id":"01J33PNP74S9EAH86CP7VQKZV1"}
def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)

# helper function so we can pass in the first/last indices
def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        # recursively sort the left / right sub-lists
        quick_sort_helper(alist, first, splitpoint - 1) # left sub-list
        quick_sort_helper(alist, splitpoint + 1, last)  # right sub-list
    
# partition function will organize left sublist < pivot
# and right sublist > pivot
def partition(alist, first, last):
    pivot = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        # step 3:
        # move leftmark until we find a left element > pivot
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark = leftmark + 1
        
        # step 4:
        # move rightmark until we find a right element < pivot
        while rightmark >= leftmark and alist[rightmark] >= pivot:
            rightmark = rightmark - 1
        
        # step 5--6:
        # check if we're done swapping left/right elements
        if rightmark < leftmark:
            done = True
        else:
            # swap left and eight elements into correct side of list
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
        
    # step 7:
    # put the pivot value into the correct place
    # (swap pivot with rightmark index)
    temp = alist[first] # pivot
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

numlist1 = [9,8,7,6,5,4,3,2,1]
numlist2 = [1,2,3,4,5,6,7,8,9]
numlist3 = []
numlist4 = [1,9,2,8,3,7,4,5,6]

quick_sort(numlist1)
quick_sort(numlist2)
quick_sort(numlist3)
quick_sort(numlist4)

assert numlist1 == [1,2,3,4,5,6,7,8,9]
assert numlist2 == [1,2,3,4,5,6,7,8,9]
assert numlist3 == []
assert numlist4 == [1,2,3,4,5,6,7,8,9]
```

## Quick Sort Analysis

* Best-case running time is $O(n log n)$.
    - In the best case, there are $log n$ levels.
      Each level is $O(n)$ when performing the partition step.
* However, the worst $O(n^2)$.
    - Consider the case where the list is already sorted
      (or in reverse order).
    - The sub lists aren't evenly divided for every recursive call.
    - Quick sort performance is dependent on the pivot value!
    - Can try to improve the pivot choice by selecting random values and choosing the medium.
    - Textbook describes the median of three approach:
        - Choose the first, middle, and last elements. Choose the median of those values.
    - But even then, there is no guarantee that these values are good pivot values, but it does improve our chances.
* Note that Quick sort __does not__ need extra space (unlike merge sort).
