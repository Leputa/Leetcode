from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s = list(s)
        ret = []
        self.traceback(s, ret, [], len(s))
        return ret

    def traceback(self, s, ret, tmpList, all_length):
        length = sum([len(palindrome) for palindrome in tmpList])
        if length == all_length:
            ret.append(tmpList[:])
            return

        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                tmpList.append("".join(s[:i+1]))
                self.traceback(s[i+1:], ret, tmpList, all_length)
                tmpList.pop()

    def isPalindrome(self, s):
        if len(s) == 0:
            return False
        low, high = 0, len(s)-1
        while(low < high):
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True


if __name__ == "__main__":
    print(Solution().partition("aa"))