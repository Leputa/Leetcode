from typing import List

class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        numerator, denominator = 0, 0 # fenzi, fenmu = 0, 0
        for a in cont[::-1]:
            if denominator == 0:  # fenmu. = 0
                denominator = 1   # fenmu  = 1
                numerator = a    # fenzi = a     
            else:
                denominator_back = denominator
                denominator = numerator
                numerator = denominator_back
                numerator = a * denominator + numerator  # fenzi = fenmu + a * fenmu
                
        # for i in range(2, min(numerator, denominator)):
        #     if numerator % i == 0 and denominator % i == 0:
        #         numerator = numerator // i
        #         denominator = denominator // i
        
        return [numerator, denominator]


if __name__ == "__main__":
    print(Solution().fraction([3]))


