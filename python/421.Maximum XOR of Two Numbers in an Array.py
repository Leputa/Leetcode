class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        flag=0
        for i in range(31,-1,-1):
        	prefixSet=set()
        	#flag:1111000000......
        	flag=flag|(1<<i)
        	for num in nums:
        		prefixSet.add(num&flag) #保存高i位的1
        	#将tmp下一个地位置为1
        	tmp=max|(1<<i)
        	for prefix in prefixSet:
        		#a^b=c则b^c=a
        		#查看tmp(即max)能否将下一个 低位 置为1
                #max^prefix=tmp tmp^prefix=max
        		if tmp^prefix in prefixSet:
        			max=tmp
        			break
        return max
