class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit=0
        length=len(digits)-1
        for i in digits:
        	digit+=i*pow(10,length)
        	length-=1
        digit+=1

        res=[]
        while(digit!=0):
        	res.append(digit%10)
        	digit/=10
        return res[::-1]
