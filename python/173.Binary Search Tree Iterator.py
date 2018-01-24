# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root=root
        self.stack=[]
        temp=root
        while(temp!=None):
            self.stack.append(temp)
            temp=temp.left
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return not len(self.stack)==0
        

    def next(self):
        """
        :rtype: int
        """
        tempNode=self.stack.pop()
        temp=tempNode.right
        while(temp!=None):
            self.stack.append(temp)
            temp=temp.left
        return tempNode.val
