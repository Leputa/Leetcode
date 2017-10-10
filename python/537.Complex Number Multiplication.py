class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lista=a.split('+')
        listb=b.split('+')

        numa=int(lista[0])
        numb=int(listb[0])

        num=numa*numb

        taga=0
        tagb=0

        if lista[1][0]=='-':
        	taga=-1
        numai=int(lista[1][:len(lista[1])-1])

        if listb[1][0]=='-':
        	tagb=-1
        numbi=int(listb[1][:len(listb[1])-1])

        num-=numai*numbi

        numi=numa*numbi+numb*numai

        return str(num)+'+'+str(numi)+'i'

        

