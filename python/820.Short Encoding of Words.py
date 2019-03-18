class Solution:
    def minimumLengthEncoding(self, words):
        if len(words) == 0:
            return 0
        if len(words) == 1:
            return len(words[0]) + 1
        
        for i in range(len(words)):
            words[i] = words[i][::-1]
        words = sorted(words, reverse=True)
        ret = 0
        idx = 0
        while idx < len(words)-1:
            tag = 0
            for j in range(idx+1, len(words)):
                if not words[idx].startswith(words[j]):
                    tag = 1
                    break
            ret = ret + len(words[idx]) + 1
            idx = j
        if tag == 1:
            ret += len(words[len(words)-1]) + 1
        return ret

print(Solution().minimumLengthEncoding(["t"]))
