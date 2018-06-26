class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
            
        pRootCopy = self.TreeCopy(pRoot)
        pRootCopy = self.TreeChange(pRootCopy)

        return self.isSameTree(pRoot, pRootCopy)

    def isSameTree(self, pRoot, pRootCopy):
        if pRoot == None and pRootCopy == None:
            return True
        elif pRoot == None:
            return False
        elif pRootCopy == None:
            return False
        elif pRoot.val != pRootCopy.val:
            return False

        tagleft = self.isSameTree(pRoot.left, pRootCopy.left)
        tagright = self.isSameTree(pRoot.right, pRootCopy.right)

        return tagleft and tagright


    def TreeCopy(self, pRoot):
        # 复制一棵树
        pRootCopy = TreeNode(pRoot.val)
        if pRoot.left != None:
            pRootCopy.left = self.TreeCopy(pRoot.left)
        if pRoot.right != None:
            pRootCopy.right = self.TreeCopy(pRoot.right)
        return pRootCopy

    def TreeChange(self, pRoot):
        # 求一棵树的镜像
        tmpNode = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = tmpNode

        if pRoot.left != None:
            pRoot.left = self.TreeChange(pRoot.left)
        if pRoot.right != None:
            pRoot.right = self.TreeChange(pRoot.right)
        return pRoot
