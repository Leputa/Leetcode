class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for s in S:
            if s == "(":
                stack.append(s)
            else:
                if len(stack) != 0 and stack[len(stack)-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    tmp = 0
                    while (len(stack) != 0 and stack[len(stack)-1] != "("):
                        tmp += stack.pop()
                    if len(stack) != 0:
                        stack.pop()
                        tmp *= 2
                    stack.append(tmp)
        
        return sum(stack)

print(Solution().scoreOfParentheses("()(())"))