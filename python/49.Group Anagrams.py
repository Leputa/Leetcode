import operator

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        big_dic = {}  # dic->list
        for string in strs:
            tag = 0
            dic = {}
            for s in string:
                dic[s] = dic.get(s, 0) + 1

            for key, val in big_dic.items():
                if operator.eq(val[0], dic) == True:
                    val.append(string)
                    tag = 1
                    break
            if tag == 0:
                big_dic[string] = [dic, string]
        
        res = []
        for key, val in big_dic.items():
            res.append(val[1:])
        return res

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# 上述解法超时了
# 想试一下对string排序，但速度只会更慢，照理来说也会超时（看了别人的代码发现不会超时....ORZ）



