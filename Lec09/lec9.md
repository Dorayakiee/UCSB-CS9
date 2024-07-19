% Lecture 9
% Tue Jul 16, 2024

* Lab06 and Lab07
* Homework h06 and h07
* Quiz 3
* Quadratic-time sorting algorithms:
    - Selection sort
    - Insertion sort

# Bubble sort review

**Idea:** Bubble sort will make several passes through the list and swap adjacent elements to ensure the largest element ends up at the end of the list.

```
First pass:

(5 1) 4 2 8 --> (1 5) 4 2 8
1 (5 4) 2 8 --> 1 (4 5) 2 8
1 4 (5 2) 8 --> 1 4 (2 5) 8
1 4 2 (5 8) --> 1 4 2 (5 8)

Second pass:

(1 4) 2 5 [8] --> (1 4) 2 5 [8]
1 (4 2) 5 [8] --> 1 (2 4) 5 [8]
1 2 (4 5) [8] --> 1 2 (4 5) [8]

Third pass:

(1 2) 4 [5 8] --> (1 2) 4 [5 8]
1 (2 4) [5 8] --> 1 (2 4) [5 8]

Fourth pass:

1 2 [4 5 8] --> 1 2 [4 5 8]

No swaps, we can stop.
```

# Selection Sort

**Idea:** Similar to bubble sort, we make passes through the list and find the largest element. We then swap the largest element in the correct place (each iteration will place the largest element at the end of the list).

```python {"id":"01J2YJB56G6W3F8YBC2797WJ5Q"}
def selection_sort(l):
    for swap_index in range(len(l) - 1, 0, -1):
        # find the largest value
        index_of_max = 0
        for location in range(1, swap_index + 1):
            if l[location] > l[index_of_max]:
                index_of_max = location
        
        # swap largest element into its correct spot
        temp = l[swap_index]
        l[swap_index] = l[index_of_max]
        l[index_of_max] = temp

l1 = [1,2,3,4]
selection_sort(l1)
assert(l1 == [1,2,3,4])

l2 = [11,20,3,4]
selection_sort(l2)
assert(l2 == [3,4,11,20])

l3 = [11,11,11,11]
selection_sort(l3)
assert(l3 == [11,11,11,11])

l4 = []
selection_sort(l4)
assert(l4 == [])
```

## Selection sort analysis

* Similar to bubble sort, we have to make n-1 comparisons during the first iteration through the list.
    - Then n-2 comparisons durint the 2nd iteration, etc.
* If we count the number of comparisons in this algorithm, we have:
    - $(n-1) + (n-2) + (n-3) + ... + 2 + 1 = n(n+1) / 2$
    - $O(n^2)$
* Note: We only do _one_ swap operation per iteration unlike Bubble sort.

# Insertion Sort

**Idea:** We want to work left-to-right and insert unsorted elements into the sorted left portion of the list.

* For example, the first element is sorted by default.
* Then we check the second element, and detemine if it goes before, middle, or after the first two (sorted) elements. And so on...
* Note that in order to make "room" for the inserted element, we have to shift the elements greater than the inserted element up by one.
* Analogy: Similar to sorting a deck of cards. Work left-to-right, take a card and insert it into the correct position on the left portion of the sorted deck.

```python {"id":"01J2YKBYGP7789JN1M2BCBQPTM"}
def insertion_sort(l):
    for index in range(1, len(l)):

        current_value = l[index]
        position = index

        # shift elements over by one
        while position > 0 and l[position - 1] > current_value:
            l[position] = l[position - 1]
            position = position - 1
        
        # insert element in appropriate place
        l[position] = current_value


l1 = [1,2,3,4]
insertion_sort(l1)
assert(l1 == [1,2,3,4])

l2 = [11,20,3,4]
insertion_sort(l2)
assert(l2 == [3,4,11,20])

l3 = [11,11,11,11]
insertion_sort(l3)
assert(l3 == [11,11,11,11])

l4 = []
insertion_sort(l4)
assert(l4 == [])
```

## Insertion sort analysis

* When we check where to insert an element, we do up to 1 swap on the first iteration in order to make room for the element to be inserted in the sorted left portion of the list.
    - Then we do up to two swaps on the second iteration
    - Then up to three swaps on the third iteration, etc.
    - $1 + 2 + ... + (n-2) + (n-1)$ swaps
    - $O(n^2)$
* Let's also look at the BEST case scenario (the list is already sorted)
    - Here, we still go through n elements, but no swaps occur because each position is in the correct place.
    - So in the base case scenario, we have $O(n)$.