# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        tmpNode = root
        preVisitNode = None
        rnt = []

        while(tmpNode!= None or len(stack)!=0):

            while(tmpNode != None):
                stack.append(tmpNode)
                tmpNode = tmpNode.left

            if len(stack)!=0:
                tmpNode = stack[len(stack)-1]
                if tmpNode.right == None or tmpNode.right == preVisitNode:
                    stack.pop()
                    rnt.append(tmpNode.val)
                    preVisitNode = tmpNode
                    tmpNode = None
                else:
                    tmpNode = tmpNode.right   
        return rnt
        

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().postorderTraversal(root))

