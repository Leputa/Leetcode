
def max_score(goals, balls):
    if len(goals) == 0 or len(balls) == 0:
        return 0
    goals = sorted(goals, key = lambda info: info[0])
    combine_goals = []
    
    pre_a = goals[0][0]
    pre_b = goals[0][1]

    for i in range(1, len(goals)):
        goal = goals[i]
        a, b = goal[0], goal[1]
        if a <= pre_b:
            pre_b = max(pre_b, b)
        else:
            combine_goals.append([pre_a, pre_b])
            pre_a = a
            pre_b = b
    combine_goals.append([pre_a, pre_b])
    balls = sorted(balls)
    
    cnt = 0 
    i, j = 0, 0
    while(j < len(balls) and i < len(combine_goals)):
        if balls[j] >= combine_goals[i][0] and balls[j] <= combine_goals[i][1]:
            cnt += 1
            j += 1
        elif balls[j] < combine_goals[i][0]:
            j += 1
        else:
            i += 1
    return cnt 



if __name__ == "__main__":
    # n, m = list(map(int, input().split(" ")))
    # goals = []
    # for i in range(n):
    #     goals.append(list(map(int, input().split(" "))))
    # balls = []
    # for j in range(m):
    #     balls.append(int(input()))
    # print(max_score(goals, balls))
    print(max_score([[2, 6], [3, 4], [8, 10], [13, 15]], [14, 0, 2, 4, 7, 9, 10]))
