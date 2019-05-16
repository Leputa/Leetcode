# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack = []
        root = TreeNode(preorder[0])
        stack.push(root)
        for i in range(1, len(preorder)):
            tmpNode = TreeNode(preorder[i])
            if preorder[i] < stack[len(stack)-1].val:
                stack[len(stack)-1].left = tmpNode
                stack.append(tmpNode)
            else:
                while(len(stack) > 1 and stack[len(stack)-2].val < preorder[i]):
                    stack.pop()
                if len(stack) == 1:
                    stack[len(stack)-1].right = tmpNode
                    stack.pop()
                    stack.append(tmpNode)
        return root


