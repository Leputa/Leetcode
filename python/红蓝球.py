
def get_prob(m, n):
    '''
    m个红球
    n个蓝球 
    '''
    if m == 0:
        return 0

    p_a = m / (m+n)
    if m + n - 2 <= 0:
        return p_a
    
    p_b = n / (m+n) * (n-1) / (m+n-1) #ab拿蓝球
    return p_a + p_b * (get_prob(m-1, n-2) * m/(m+n-2) + get_prob(m, n-3) * (n-2)/(m+n-2))
    

if __name__ == "__main__":
    m, n = list(map(int, input().split(" ")))
    print(format("%.5f"%get_prob(m, n))) 
