
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
    
    def hasLeftChild(self):
        return self.left_child  # Note: None equates to False
    
    def hasRightChild(self):
        return self.right_child
    
    def isLeftChild(self):
        return self.parent and self.parent.left_child == self 

    def isRightChild(self):
        return self.parent and self.parent.right_child == self
    
    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right_child or self.left_child)
    
    def hasAnyChildren(self):
        return self.right_child or self.left_child
    
    def hasBothChildren(self):
        return self.right_child and self.left_child

    def replaceNodeData(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right

        if self.hasLeftChild():
            self.left_child.parent = self
        if self.hasRightChild():
            self.right_child.parent = self
        