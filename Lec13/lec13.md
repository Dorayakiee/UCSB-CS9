% Lecture 13
% Wed Jul 24, 2024

Today:

* Binary trees
* Tree traversal algorithms
* Binary search trees (BST)

# Binary Trees

* Recall: A binary tree is a tree structure where a node has __at most__ two children.
* So far we've talked about trees conceptually when analyzing sorting algorithms (merge sort/quick sort).
* We even talked about how to implement Min/Max Heaps (conceptualized as complete binary trees).

## Nodes and Reference Representation

* Similar to our Linked List implementation, we can expand upon this concept using nodes and references to construct our tree.
* Each node can be represented as an object
    - Each node will have left / right child references to other nodes in the tree.
    - Each node is the "root" of its own subtree.

```python {"id":"01J3K4XZ3WCAZMYCTMKJ5AACDC"}
class BinaryTreeNode:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild
    
    def getRootValue(self):
        return self.key
    
    def setRootVal(self, obj):
        self.key = obj
    
    def insertLeft(self, newNode):
        # Case 1: Node does not have a left child
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a left child
            t = BinaryTreeNode(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        # Case 1: Node does not have a right child
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a right child
            t = BinaryTreeNode(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

node = BinaryTreeNode("A")
assert node.getRootValue() == "A"
assert node.getLeftChild() == None
assert node.getRightChild() == None

node.insertLeft("B")
assert node.getLeftChild().getRootValue() == "B"
assert node.getRootValue() == "A"
assert node.getRightChild() == None
assert node.getLeftChild().getRightChild() == None
assert node.getLeftChild().getLeftChild() == None

node.insertRight("C")
assert node.getRightChild().getRootValue() == "C"
assert node.getRightChild().getLeftChild() == None
assert node.getRightChild().getRightChild() == None

node.insertLeft("D")
assert node.getLeftChild().getRootValue() == "D"

temp = node
s = ""
while temp != None:
    s = s + temp.getRootValue()
    temp = temp.getLeftChild()
print(s)

assert node.getLeftChild().getLeftChild().getRootValue() == "B"

```

# Tree Traversal

* Sometimes we want to visit all the nodes in a tree.
* We can do this in various ways, with varying orders.
* There are three common ways to traverse nodes in a tree:
    - Pre-order:
        1. Vist the node
        2. Recurse on its left subtree
        3. Recurse on its right subtree
    - In-order:
        1. Recurse on its left subtree
        2. Vist the node
        3. Recurse on its right subtree
    - Post-order:
        1. Recurse on its left subtree
        2. Recurse on its right subtree
        3. Vist the node

```python {"id":"01J3K6ZNRJD5ZJFZX7P4ADCWMF"}
class BinaryTreeNode:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild
    
    def getRootValue(self):
        return self.key
    
    def setRootVal(self, obj):
        self.key = obj
    
    def insertLeft(self, newNode):
        # Case 1: Node does not have a left child
        if self.leftChild == None:
            self.leftChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a left child
            t = BinaryTreeNode(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        # Case 1: Node does not have a right child
        if self.rightChild == None:
            self.rightChild = BinaryTreeNode(newNode)
        else: # Case 2: Node has a right child
            t = BinaryTreeNode(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

def preorder(tree):
    order = ""
    if tree != None:
        order += tree.getRootValue()
        order += preorder(tree.getLeftChild())
        order += preorder(tree.getRightChild())
    return order

def inorder(tree):
    order = ""
    if tree != None:
        order += inorder(tree.getLeftChild())
        order += tree.getRootValue()
        order += inorder(tree.getRightChild())
    return order

def postorder(tree):
    order = ""
    if tree != None:
        order += postorder(tree.getLeftChild())
        order += postorder(tree.getRightChild())
        order += tree.getRootValue()
    return order

root = BinaryTreeNode("A")
root.insertLeft("D")
root.insertLeft("B")
root.insertRight("C")
root.getRightChild().insertLeft("E")
root.getRightChild().insertRight("F")

assert preorder(root) == "ABDCEF"
assert inorder(root) == "DBAECF"
assert postorder(root) == "DBEFCA"
```

# Binary Search Tree (BST)

* Recall that a binary tree is a tree where a node may have at most two children.
* **Binary Search Trees** (BSTs) are binary trees that have the following property:
    - Values that are less than the parent are in the left subtree
    - Values that are greater than the parent are in the right subtree
* This is the "BST property".

* BSTs are also one way to implement a "Map" abstract data type.
    - A Map data type maps keys to corresponding values.
    - Think of keys defining _where_ in the BST structure a node gets inserted.
    - And each node has a corresponding value field.
    - Similar to how Python Dictionaries work at a high level.

* Note: Insertion order affects the structure of the tree!
* Also note: In-order traversal in a BST will visit the nodes in order!
    - Try it out!