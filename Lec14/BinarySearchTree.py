
from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        # A BST just needs a reference to the root node
        self.root = None
        self.size = 0 # Keeps track of the number of nodes
    
    def length(self):
        return self.size

    def put(self, key, val):
        if self.root == None:
            self.root = TreeNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size = self.size + 1
    
    # helper method to recursively walk the tree
    # and find the right place to insert the new node
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.hasLeftChild():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:
            if current_node.hasRightChild():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
    

    # dict[key] --> value, dict.get(key)
    # return the value of the key if it exists
    def get(self, key):
        if self.root:
            result_node = self._get(key, self.root)
            if result_node:
                return result_node.val
            else:
                return None
        else:
            return None
    
    # helper method to recursively walk the tree
    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
    