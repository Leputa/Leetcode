class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = "1"
        for i in range(1,n):
            tmpRet = ""
            #切分ret,记录每段的长度和值
            cnt = 1
            for j in range(1,len(ret)):
                if ret[j]==ret[j-1]:
                    cnt +=1
                else:
                    tmpRet += str(cnt)+ret[j-1]
                    cnt = 1
            tmpRet += str(cnt)+ret[len(ret)-1]
            ret = tmpRet
        return ret

print(Solution().countAndSay(5))