class Solution:
    def minAddToMakeValid(self, S: 'str') -> 'int':
        stack = []
        ret = 0
        for s in S:
            if s == "(":
                stack.append(s)
            else:
                if len(stack) == 0:
                    ret += 1
                else:
                    stack.pop()
        ret += len(stack)
        return ret