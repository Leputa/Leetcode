class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        length = len(words[0])
        ret = []
        dic = {}

        if length==0 or len(s)==0:
            return ret

        for word in words:
            dic[word] = dic.get(word,0)+1

        for i in range(len(s)-length*len(words)+1):
            wordMap = dic.copy()
            tmpString = s[i:i+length]
            j = i
            while wordMap.get(tmpString,0)!=0:
                wordMap[tmpString] -=1
                if wordMap[tmpString] == 0:
                    del wordMap[tmpString]
                    if len(wordMap) == 0:
                        ret.append(i)
                        break
                j += length
                tmpString = s[j:j+length]
                
        return ret
            


print(Solution().findSubstring("barfoothefoobarman",["foo","bar"]))