class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic={}
        for i in range(ord('a'),ord('z')+1):
        	dic[chr(i)]=[501,-1]
        for i in range(len(S)):
        	if dic[S[i]][0]>i:
        		dic[S[i]][0]=i
        	if dic[S[i]][1]<i:
        		dic[S[i]][1]=i
        #sorted(dic.items(),key=lambda x:x[1][0])
        keys=dic.keys()
        values=dic.values()
        list_one=[(key,val) for key,val in zip(keys,values)]
        dic=sorted(list_one,key=lambda x:x[1][0])
       	dic=list(filter(lambda x:x[1][0]!=501,dic))
        ans=[]
        end=0
        start=0
        for key in dic:
        	value=key[1]
        	if value[0]==0:
        		start=value[0]
        		end=value[1]
        	elif value[0]>end:
        		ans.append(end-start+1)
        		start=value[0]
        		end=value[1]
        	elif value[0]<end and value[1]>end:
        		end=value[1]
        ans.append(end-start+1)
        return ans


print(Solution().partitionLabels("oiehdsofhsadohsdakfh"))