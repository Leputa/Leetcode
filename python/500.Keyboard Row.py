class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        str1=['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
        str2=['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
        str3=['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']

        length=len(words)
        tag=0
        flag=0
        ans=[]

        for i in range(length):
            TT=True
            if words[i][0] in str1:
                tag=1
            if words[i][0] in str2:
                tag=2
            if words[i][0] in str3:
                tag=3
            for j in words[i]:
                if j in str1:
                    flag=1
                if j in str2:
                    flag=2
                if j in str3:
                    flag=3
                if tag!=flag:
                    TT=False
                    break
            if TT==True:
                ans.append(words[i])
        return ans




print(Solution().findWords(["abdfs","cccd","a","qwwewm"]))