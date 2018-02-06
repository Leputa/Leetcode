class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans=0
        for i in S:
        	if i in J:
        		ans+=1
        return ans