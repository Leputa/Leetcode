class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathList = path.strip().split("/")
        stack = []
        for x in pathList:
            if x == '.' or x=='':
                continue
            elif x == '..':
                if len(stack)==0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(x)

        ret = ''
        for x in stack:
            ret += '/'+x

        if len(ret) == 0:
            return '/'
        return ret


print(Solution().simplifyPath("/"))




