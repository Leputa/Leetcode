class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dictRes={}
        restaurant=[]
        indexSum=2000
        for i in range(len(list1)):
        	dictRes[list1[i]]=i
        for j in range(len(list2)):
        	if dictRes.get(list2[j])!=None :
        		if dictRes[list2[j]]+j<indexSum:
        			indexSum=dictRes[list2[j]]+j
        			restaurant=[]
        			restaurant.append(list2[j])
        		elif dictRes[list2[j]]+j==indexSum:
        			restaurant.append(list2[j])
        return restaurant



        


print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Burger King", "Tapioca Express", "Shogun"]))
