# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, summ: int) -> List[List[int]]:
        ret = []
        if root == None:
            return ret
        self.get_path(root, [], ret, summ)
        return ret

    def get_path(self, tmpNode, tmplist, ret, summ):
        tmplist.append(tmpNode.val)
        if tmpNode.left == None and tmpNode.right == None:
            if sum(tmplist) == summ:
                ret.append(tmplist[:])
            return 
        if tmpNode.left != None:
            self.get_path(tmpNode.left, tmplist, ret, summ)
            tmplist.pop()
        if tmpNode.right != None:
            self.get_path(tmpNode.right, tmplist, ret, summ)
            tmplist.pop()
