class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        self.dive(root, val)
        return root

    def dive(self, root: 'TreeNode', val: 'int') -> 'None':
        if val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.dive(root.right, val)
        else:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.dive(root.left, val)