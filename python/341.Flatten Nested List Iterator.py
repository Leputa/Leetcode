# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        sb=nestedList[::-1]
        self.ans=[]
        self.dfs(nestedList)
        self.index=0
        self.length=len(self.ans)

    def dfs(self,nestedList):
        for nest in nestedList:
            if(type(nest).__name__=='list'):
                self.dfs(nest)
            else:
                self.ans.append(nest)

    def next(self):
        """
        :rtype: int
        """
        self.index+=1
        return self.ans[self.index-1]
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index<self.length

i,v=NestedIterator([[1,1],2,[1,1]]),[]
while(i.hasNext()):
    v.append(i.next())
print(v)