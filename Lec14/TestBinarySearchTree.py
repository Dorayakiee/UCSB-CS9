
from BinarySearchTree import BinarySearchTree

def test_constructBST():
    BST = BinarySearchTree()
    assert BST.root == None
    assert BST.length() == 0

def test_insertRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    assert BST.root.key == 10
    assert BST.root.val == "ten"
    assert BST.root.hasLeftChild() == None
    assert BST.root.hasRightChild() == None
    assert BST.root.isLeftChild() == None
    assert BST.root.isRightChild() == None
    assert BST.root.isRoot() == True
    assert BST.root.hasAnyChildren() == None
    assert BST.root.isLeaf() == True

    BST.root.replaceNodeData(20, "twenty", None, None)
    assert BST.root.key == 20
    assert BST.root.val == "twenty"

def test_insertNodes():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(20, "twenty")
    BST.put(15, "fifteen")
    BST.put(5, "five")

    assert BST.root.key == 10
    assert BST.root.left_child.key == 5
    assert BST.root.right_child.key == 20
    assert BST.root.right_child.left_child.key == 15

def test_getValues():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(20, "twenty")
    BST.put(15, "fifteen")
    BST.put(5, "five")

    assert BST.get(20) == "twenty"
    assert BST.get(123123) == None