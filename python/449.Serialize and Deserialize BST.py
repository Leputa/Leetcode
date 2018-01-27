# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans=''
        if (root==None):
            return ans
        ans+=str(root.val)
        if root.left!=None:
            ans+=','+self.serialize(root.left)
        if root.right!=None:
            ans+=','+self.serialize(root.right)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(len(data)==0):
            return None
        dataList=data.strip().split(',')
        dataList=list(map(int,dataList))
        return self.dfs(dataList)

    def dfs(self,data):
        if len(data)==0:
            return None
        root=TreeNode(data[0])
        if len(data)==1:
            return root
        index=-1
        for i in range(1,len(data)):
            if data[i]>data[0]:
                index=i
                break
        if index==-1:
            index=len(data)
        root.left=self.dfs(data[1:index])
        root.right=self.dfs(data[index:])
        return root


