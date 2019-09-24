
def exchange_prefix(strs, n, m):
    ret = 1
    list_set = [[] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            list_set[j].append(strs[i][j])
    for j in range(m):
        ret = (ret * len(set(list_set[j]))) % 1000000007
    return ret


if __name__ == "__main__":
    n, m = list(map(int, input().split(" ")))
    strs = []
    for i in range(n):
        strs.append(input())
    print(exchange_prefix(strs, n, m))
    #print(exchange_prefix(["ABC", "DEF"], 2, 3))