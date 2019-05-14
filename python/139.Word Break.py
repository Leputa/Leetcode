from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        cache = [-1] * (len(s)+1)
        return self.check(s, wordDict, 0, cache)

    def check(self, s, wordDict, start, cache):
        if start >= len(s):
            return True
        if cache[start] == 0:
            return False
        if cache[start] == 1:
            return True

        for i in range(start+1, len(s)+1):
            if s[start:i] in wordDict and self.check(s, wordDict, i, cache):
                cache[i] = 1
                return True
        cache[start] = False
        return False
        


if __name__ == "__main__":
    print(Solution().wordBreak("a", ["b"]))
