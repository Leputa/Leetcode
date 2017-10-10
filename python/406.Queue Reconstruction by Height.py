class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def my_key(pp):
            return -pp[0],pp[1]#表示按第一个键降序 第二个键升序
        people.sort(key=my_key)
        #print(people)
        for i in range(len(people)):
            if i>=len(people):
                break
            if(people[i][1]==i):
                continue
            tmp=people[i]
            people.pop(i)
            people.insert(tmp[1],tmp) #tmp[1]为插入位置
        return people
Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])