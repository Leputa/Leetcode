from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s = Counter(s)
        odd = 0
        for key, val in s.items():
            if val % 2 != 0:
                odd += 1
                if odd > 1:
                    return False
        return True


print(Solution().canPermutePalindrome("tactcoa"))