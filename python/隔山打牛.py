

def damage(enemies):
    cnt = 0
    pos = 1
    while (pos <= len(enemies)):
        while (enemies[pos-1] > 0 and (2 * pos - 1 < len(enemies) and enemies[2 * pos - 1] > 0) and (2 * pos  < len(enemies) and enemies[2 * pos] > 0)):
            enemies[pos-1] -= 1
            if 2 * pos - 1 < len(enemies):
                enemies[2 * pos - 1] -= 1
            if 2 * pos < len(enemies):
                enemies[2 * pos] -= 1
            cnt += 1
        pos += 1

    pos = 1
    while (pos <= len(enemies)):
        while ((enemies[pos-1] > 0 and (2 * pos - 1 < len(enemies) and enemies[2 * pos - 1] > 0)) \
            or (enemies[pos-1] > 0 and 2 * pos < len(enemies) and enemies[2 * pos] > 0) 
            or ((2 * pos - 1 < len(enemies) and enemies[2 * pos - 1] > 0) and  2 * pos < len(enemies) and enemies[2 * pos] > 0)):
            enemies[pos-1] -= 1
            if 2 * pos - 1 < len(enemies):
                enemies[2 * pos - 1] -= 1
            if 2 * pos < len(enemies):
                enemies[2 * pos] -= 1
            cnt += 1
        pos += 1

    pos = 1 
    while(pos <= len(enemies)):
        while(enemies[pos-1] > 0):
            enemies[pos-1] -= 1
            cnt += 1
        pos += 1

    return cnt


if __name__ == "__main__":
    # n = int(input())
    # enemies = list(map(int, input().split(" ")))
    # print(damage(enemies))
    print(damage([1, 2, 3, 4, 5]))

