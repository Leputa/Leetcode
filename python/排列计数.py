

global cnt
global mod 
mod = 10**9 + 7

def permutation(N, A):
    inputs = [i for i in range(1, N+1)]
    tags = [False] * N
    global cnt 
    cnt = 0
    trace_back(inputs, tags, [], A)
    return cnt

def trace_back(inputs, tags, tmpList, A):
    if len(tmpList) == len(inputs):
        global cnt
        global mod
        cnt = (cnt + 1)%mod
        return
    for i in range(len(inputs)):
        if tags[i] == False:
            if len(tmpList) == 0:
                tags[i] = True
                tmpList.append(inputs[i])
                trace_back(inputs, tags, tmpList, A)
                tmpList.pop()
                tags[i] = False
            else:
                position = len(tmpList)-1
                if A[position] == 1 and inputs[i] < tmpList[-1]:
                    tags[i] = True
                    tmpList.append(inputs[i])
                    trace_back(inputs, tags, tmpList, A)
                    tmpList.pop()
                    tags[i] = False
                if A[position] == 0 and inputs[i] > tmpList[-1]:
                    tags[i] = True
                    tmpList.append(inputs[i])
                    trace_back(inputs, tags, tmpList, A)
                    tmpList.pop()
                    tags[i] = False

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split(" ")))
    print(permutation(N, A))

