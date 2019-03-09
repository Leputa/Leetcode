class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while len(stack) != 0 and  stack[len(stack) - 1] == popped[idx]:
                stack.pop()
                idx += 1
        
        if idx == len(popped) and len(stack) == 0:
            return True
        else:
            return False



