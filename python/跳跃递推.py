def recursion(a, n):
    if n <= 4:
        return a[n-1]
    for i in range(4, n):
        a[i%4] = a[(i-1) % 4] + a[(i-3) % 4] + a[(i-4)%4]
        if i == n-1:
            return a[i%4]
        #a.append(a[i-1] + a[i-3] + a[i-4])
    #return a[-1]

if __name__ == "__main__":
    x = list(map(int, input().split(" ")))
    a = x[:-1]
    n = x[-1]
    print(recursion(a, n))
    # print(recursion([1, 2, 3, 4], 20))
