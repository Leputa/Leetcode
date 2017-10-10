class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        self.keySet=[]
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if self.dic.get(key)==None:
            self.dic[key]=val
            self.keySet.append(key)
        else:
            self.dic[key]=val

        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ans=0
        for i in self.keySet:
            if i.startswith(prefix):
                ans+=self.dic[i]
        return ans

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)