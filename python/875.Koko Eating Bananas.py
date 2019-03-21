import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        high,low = max(piles), 0
        hour = len(piles)
        if hour == H:
            return high
        if hour == 1:
            return math.ceil(piles[0]/H)
        while low < high:
            mid = (high + low) // 2
            new_hour = 0
            for pile in piles:
                new_hour += math.ceil(pile/mid)
            if new_hour <= H:
                high = mid
            else:
                low = mid + 1
        return low
                
                
            

