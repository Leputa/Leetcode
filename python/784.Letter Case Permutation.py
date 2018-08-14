class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.traceback(list(S), 0, res, '')
        return res

    def traceback(self, S, i, res, ans):
        if i == len(S):
            res.append(ans)
            return 

        if S[i].isalpha():
            self.traceback(S, i+1, res, ans + S[i])
            if S[i] >= 'a' and S[i] <= 'z':
                S[i] = S[i].upper()
            else:
                S[i] = S[i].lower()
            self.traceback(S, i+1, res, ans + S[i])
        else:
            self.traceback(S, i+1, res, ans + S[i])

    

if __name__ == '__main__':
    print(Solution().letterCasePermutation("a1b2"))
