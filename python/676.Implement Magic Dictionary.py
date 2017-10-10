class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic=[]
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            self.dic.append(i)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in self.dic:
            if self.isOneChange(i,word):
                return True
        return False
    def isOneChange(self,word1,word2):
        if len(word1)!=len(word2):
            return False
        cnt=0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                cnt+=1
            if cnt>=2:
                return False
        if cnt==1:
            return True
        else:
            return False

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

obj=MagicDictionary()
obj.buildDict(["hello","leetcode"])
print(obj.search("hhllo"))