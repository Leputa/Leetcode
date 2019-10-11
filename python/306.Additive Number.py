

class Solution:
    def isAdditiveNumber(self, S: str) -> bool:
        return self.trace_back(S, [])


    def trace_back(self, S, path):
        if len(path) >= 3:
            if path[-1] != path[-2] + path[-3]:
                return False
            if len(S) == 0:
                return True
        cur = ""
        for i in range(len(S)):
            cur += S[i]
            if cur.startswith("0") and len(cur) > 1:
                return False
            path.append(int(cur))
            if self.trace_back(S[i+1:], path):
                return True
            path.pop()
        return False


if __name__ == "__main__":
    print(Solution().isAdditiveNumber("101"))