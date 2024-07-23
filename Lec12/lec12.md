% Lecture 12
% Tue Jul 23, 2024

* Quiz 4 graded.
* Lab08 and h08 released.
* Today:
    - Trees,
    - Priority Queues,
    - Heaps.

# Trees

## Terminology

* Node - An element in the tree. May have an incoming edge and many outgoing
  edges.
* Edge - A connection between nodes (can be directional or bidirectional)
* Root - The top most node (node without any incoming edges)
* Path - The sequence of nodes from one node to a destination node along the
  tree
* Children - Nodes that have incoming edges from another node
* Parent - Contains outgoing edges to other child nodes
* Sibling - Nodes that have the same parent
* Subtree - A tree structure where the root of the tree is a child of a parent
* Leaf - A node without any outgoing edges
* Level - Number of edges from the root node to a destination node
* Height - Maximum level of the entire tree

# Tree Properties

* <b>Binary Tree:</b> Any node may have at most two children
* <b>Balanced Binary Tree:</b> The left and right subtress of every node differ
  in height by no more than 1
* <b>Complete Tree:</b> A binary tree where every level of the tree, except the
  deepest, must contain as many nodes as possible. The deepest level must have
  all nodes <i>to the left</i> as possible

# Priority Queues

* In a queue structure, we can insert items from the back of the queue and
  remove items at the front of the queue
    * The order of elements in the queue were dictated by when items were
      inserted into the queue
* <b>Priority Queues</b> are similar to Queues EXCEPT:
    * We can insert items into the priority queue where an item has some value
      representing a priority, and items are ordered in the priority queue with
      respect to their priority value

# Heaps

* <b>MaxHeap:</b>
    * A complete tree where the value of a node is never less than the value of
      its children

```
    5
   /  \
  3    4
 / \  /
1  0 2
```

* <b>MinHeap:</b>
    * A complete tree where the value of a node is never greater than the value
      of its children

* Heaps are an efficient way to implement a Priority Queue
    * The only element we care about when removing from the priority queue is
      the root of the heap (the min value for a minHeap and the max value for a
      maxHeap)
* Since binary heaps have the complete tree property, representing this with a
  Python List is used
    * Easier to represent the heap where the 0<sup>th</sup> element in the list
      is meaningless
    * The root of the binary heap is at index 1
* A node’s index with respect to its parent and children can be generalized as:
    * A node’s <b>parent</b> index: node_index // 2 
    * A node’s <b>left child</b> index: 2 * node_index
    * A node’s <b>right child</b> index: 2 * node_index + 1


```
    5
   /  \
  3    4
 / \  /
1  0 2

  0  1   2   3   4   5   6 
[  | 5 | 3 | 4 | 1 | 0 | 2 ]

Note: 0-index is blank.
```

## Insertion into a MaxHeap Steps

1. insert the element in the first available location
	* Keeps the binary tree complete
2. While the element’s parent is less than the element
	* Swap the element with its parent

* Insertion is O(log n) (height of tree is log n)
* Inserting elements into a MaxHeap example:

* Note that MinHeap would be the same algorithm EXCEPT we swap while the
  element's parent is <b>greater than</b> the element

## Removing Max (root) element in a MaxHeap Steps

* Since heaps are used to implement priority queues, removing the root element
  is a commonly used operation

1. Copy the root element into a variable
2. Assign the last_element in the Python List to the root position
3. While new_root is less than one of its children
	* Swap the largest child with the new_root
4. Return the original root element

* Deletion is O(log n) (height of tree is log n)
* Removing elements from a MaxHeap example:


# MinHeap Implementation (from textbook)

```python {"id":"01J3GP06F53735CQDDCEKK2MKN"}
# MinHeap
class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self,i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

# pytest
def test_BinHeap():
	bh = BinHeap()
	bh.insert(5)
	bh.insert(7)
	bh.insert(3)
	bh.insert(11)
	assert bh.delMin() == 3
	assert bh.delMin() == 5
	assert bh.delMin() == 7
	assert bh.delMin() == 11

test_BinHeap()
```