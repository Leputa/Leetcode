class Solution:
    def countDigitOne(self, n: int) -> int:
        # digits = 0
        # while(n):
        #     digits += 1
        #     n /= 10
        if n <= 0:
            return 0
        
        right = 0
        coef = 1
        count = 0
        while(n):
            remaider = n % 10
            left = n // 10
            
            if remaider == 1:
                count += right + 1
            elif remaider > 1:
                count += coef
            count += coef * left
            right += coef * remaider
            coef *= 10
            n //= 10
            
        return count




