class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        code_set = list()
        gray_code = [0] * n
        self.traceback(gray_code, code_set, n)
        ans = []
        for code in code_set:
            tmp_ans = 0
            for i in range(len(code)):
                tmp_ans += code[i] * 2**(n-i-1)
            ans.append(tmp_ans)
        return ans


    def traceback(self, gray_code, code_set, n):
        for i in range(n):
            if tuple(gray_code) not in code_set:
                code_set.append(tuple(gray_code))
                self.traceback(gray_code, code_set, n)
            
            gray_code[i] = (gray_code[i] + 1) % 2
            
            if tuple(gray_code) not in code_set:
                code_set.append(tuple(gray_code))
                self.traceback(gray_code, code_set, n)

            gray_code[i] = (gray_code[i] + 1) % 2

# 我的这个写法速度太慢， 明天看下别人怎么写的，换个语言再试试

if __name__ == '__main__':
    print(Solution().grayCode(0))