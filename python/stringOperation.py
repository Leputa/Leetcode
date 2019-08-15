
def stringOperation(string: str):
    post = reverse2post(string)
    num_stack = []
    for i in range(len(post)):
        s = post[i]
        if s.isdigit():
            num_stack.append(int(s))
        else:
            if s == "+":
                tmpval = num_stack.pop() + num_stack.pop()
                num_stack.append(tmpval)
            elif s == "-":
                tmpval = num_stack.pop() - num_stack.pop()
                num_stack.append(tmpval)
            elif s == "*":
                tmpval = num_stack.pop() * num_stack.pop()
                num_stack.append(tmpval)
            elif s == "/":
                tmpval = num_stack[-2] // num_stack.pop()
                num_stack.pop()
                num_stack.append(tmpval)
            if i == len(post) - 1:
                return tmpval


def reverse2post(string: str):
    post = []
    stack = []
    
    for s in string:
        if s.isdigit():
            post.append(s)
        else:
            if s == ")":
                while(stack[-1] != "("):
                    post.append(stack.pop())
                stack.pop()
            elif s == "(":
                stack.append(s)
            else:
                while len(stack) != 0 and cmp(s, stack[-1]):
                    post.append(stack.pop())
                stack.append(s)
    
    while(len(stack) != 0):
        post.append(stack.pop())
    return post

def cmp(a, b) -> bool:
    '''
    True: a的优先级更低，出栈
    '''
    if b == "(":
        return False
    if a == "+" or a == "-":
        return True
    if (a == "*" or a == "/"):
        if b == "+" or b == "-":
            return False
        else:
            return True

if __name__ == "__main__":
    string = "5+3*2+(8/4+2)*3"
    print(stringOperation(string))




