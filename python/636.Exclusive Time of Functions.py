#浪费时间题
class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        dic={}
        dic[int(logs[0].split(":")[0])]=0
        stack=[]
        stack.append(int(logs[0].split(":")[0]))
        for i in range(1,len(logs)):
        	logList=logs[i].split(":")
        	log=(int(logList[0]),int(logList[2]))
        	preLogList=logs[i-1].split(":")
        	preLog=(int(preLogList[0]),int(preLogList[2]))
        	if (logList[1]=='start'):
        		dic[log[0]]=dic.get(log[0],0)
        		if(len(stack)!=0):
        			run=stack[-1]
        			dic[run]+=log[1]-preLog[1]
        			if(preLogList[1]=="end"):
        				dic[run]-=1
        		stack.append(log[0])
        	else:
        		dic[log[0]]=dic[log[0]]+log[1]-preLog[1]
        		if(preLogList[1]=="start"):
        			dic[log[0]]+=1
        		stack.pop()
        ans=[]
        for i in range(n):
        	ans.append(dic[i])
        return ans

print(Solution().exclusiveTime(2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))


#2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
#2,["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
#8,["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11","5:start:12","6:start:14","7:start:15","1:start:24","1:end:29","7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49","0:end:54","5:start:55","5:end:59","4:start:63","4:end:66","2:start:69","2:end:70","2:start:74","6:start:78","0:start:79","0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100","1:end:102","2:start:105","2:end:109","0:end:114"]

        		
        		

