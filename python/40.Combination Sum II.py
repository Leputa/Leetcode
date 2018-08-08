class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = set()
        candidates.sort()
        tmpList = []
        self.combine(0, candidates, target, tmpList, ret)
        return [list(t) for t in ret]

    def combine(self,start,candidates,target,tmpList,res):
        if target==0:
            res.add(tuple(tmpList[:]))
            return
        if target<0:
            return 
        for i in range(start,len(candidates)):
            tmpList.append(candidates[i])
            target -= candidates[i]
            self.combine(i+1,candidates,target,tmpList,res)
            target += candidates[i]
            tmpList.pop()
# 上述解法及慢，考虑减枝

if __name__ == '__main__':
    print(Solution().combinationSum2([2,5,2,1,2], 5))

