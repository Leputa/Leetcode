# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        stack = []
        stack.append(root)

        idx_post = 0
        for idx_pre in range(1, len(pre)):
            cur_node = TreeNode(pre[idx_pre])
            pre_node = stack[len(stack)-1]
            if pre_node.left == None:
                pre_node.left = cur_node
            else:
                pre_node.right = cur_node
            stack.append(cur_node)
            while(len(stack) != 0 and idx_post < len(post) and stack[len(stack)-1].val == post[idx_post]):
                stack.pop()
                idx_post += 1
        return root


