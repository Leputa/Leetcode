from typing import List

# class Solution:
#     def avoidFlood(self, rains: List[int]) -> List[int]:
#         ans = [-1] * len(rains)

#         counter = dict()
#         for i in range(len(rains)):
#             if rains[i] != 0:
#                 if counter.get(rains[i]) == None:
#                     counter[rains[i]] = []
#                 counter[rains[i]].append(i)

#         #print(counter)

#         full_lakes = set()
#         for i in range(len(rains)):
#             if rains[i] == 0:
#                 if len(full_lakes) == 0:
#                     ans[i] = 1
#                 else:
#                     #print("before")
#                     #print("day:", i, "full_lakes: ", full_lakes)
#                     min_day = len(rains)-1
#                     dry_lake = 1
#                     is_dry = False
#                     for lake in full_lakes:
#                         index = self.binarysearch(counter[lake], 0, len(counter[lake])-1, i)
#                         day = counter[lake][index]
#                         #print("lake: ", lake, "index: ", index, "day: ", day)
#                         if day <= i:
#                             continue
#                         if day <= min_day:
#                             is_dry = True
#                             min_day = day
#                             dry_lake = lake
#                     ans[i] = dry_lake
#                     if is_dry:
#                         full_lakes.remove(dry_lake)
#                     #print("day:", i, "full_lakes: ", full_lakes)
#                     #print("after")
                        
#             else:
#                 if rains[i] in full_lakes:
#                     return []
#                 else:
#                     full_lakes.add(rains[i])

#         return ans
                    

#     def binarysearch(self, array, left, right, target):
#         """
#         查找比target大的第一个目标（其实不存在和target相等的目标，因为rains[i]==0）
#         """
#         if left >= right:
#             return left
#         mid = (left + right) // 2
#         midVal = array[mid]
#         if midVal <= target:
#             return self.binarysearch(array, mid+1, right, target)
#         else:
#             return self.binarysearch(array, left, mid, target)

# 上述解法超时

from collections import deque, defaultdict
import heapq

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        full_lakes = set()
        counter = defaultdict(deque)
        heap = []
        heapq.heapify(heap)

        for day, lake in enumerate(rains):
            counter[lake].append(day)

        for day, lake in enumerate(rains):
            if lake == 0:
                if len(full_lakes) == 0:
                    ans[day] = 1
                else:
                    if len(heap) != 0:
                        dry_day = heapq.heappop(heap)
                        dry_lake = rains[dry_day]
                        full_lakes.remove(dry_lake)
                        ans[day] = dry_lake
                    else:
                        ans[day] = 1
            else:
                if lake in full_lakes:
                    return []
                else:
                    full_lakes.add(lake)
                    counter[lake].popleft()
                    if len(counter[lake]) != 0:
                        heapq.heappush(heap, counter[lake][0])
        return ans



if __name__ == "__main__":
    print(Solution().avoidFlood([1,0,2,0]))
