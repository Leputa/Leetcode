class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return None

        root = TreeNode(pre[0])

        tag = 0
        for i in range(len(tin)):
            if tin[i] == pre[0]:
                tag = i
                break

        root.left = self.reConstructBinaryTree(pre[1:tag+1],tin[:tag])
        root.right = self.reConstructBinaryTree(pre[tag+1:],tin[tag+1:])

        return root


