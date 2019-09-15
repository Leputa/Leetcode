def max_happiness(a, b, w, x):
    '''
    '''
    discounts = [a[_] - b[_] for _ in range(len(a))]
    max_discounts = sum(discounts)
    dp = [[0] * (max_discounts+x+1) for _ in range(len(a) + 1)]


    discounted = 0 #已经获得的优惠

    for i in range(1, len(a) + 1):
        for j in range(max_discounts+x, -1, -1):
            res = discounted + discounts[i-1] + x - j
            if res < 0:
                continue
            else:    
                if j >= b[i-1]:
                    if dp[i-1][j] > dp[i-1][j-b[i-1]] + w[i-1]: 
                        dp[i][j] = dp[i-1][j]
                    else: #买， 获得心理优惠
                        dp[i][j] = dp[i-1][j-b[i-1]] + w[i-1]
                        discounted += discounts[i-1]

    return max(dp[len(a)])


if __name__ == "__main__":
    n, x = list(map(int, input().split(" ")))
    a, b, w = [], [], []
    for i in range(n):
        line = list(map(int, input().split(" ")))
        a.append(line[0])
        b.append(line[1])
        w.append(line[2])
    print(max_happiness(a, b, w, x))



