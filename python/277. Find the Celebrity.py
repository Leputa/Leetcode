# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = 0
        for i in range(1, n):
            if knows(cur, i):  # cur认识i, cur不是名人，i可能是...
                cur = i        
                               # not knows: cur不认识i， i不一定是名人， cur可能是
        return cur