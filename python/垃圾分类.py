
def rubbish(n, constraits):
    return n//2 * 2



if __name__ == "__main__":
    n, m = list(map(int, input().split(" ")))
    constraits = []
    for i in range(m):
        constraits.append(list(map(int, input().split(" "))))
    print(rubbish(n, constraits))