

def max_ability(m, workers):
    flags = [True] * len(workers)
    sorted_list = []
    
    for i in range(m):
        sorted_list.append([]) # 每台机器可以被哪些工人操作
    
    for i in range(len(workers)):
        worker = workers[i]
        sorted_list[worker[0]-1].append((i, worker[2]))
        sorted_list[worker[1]-1].append((i, worker[2]))

    ret = 0
    for i in range(m):
        if len(sorted_list[i]) != 0:  
            # sorted_list[i] = sorted(sorted_list[i], key=lambda info: info[1], reverse=True)
            _ability = 0
            pos = -1
            for worker, ability in sorted_list[i]:
                if flags[worker] == True and ability > _ability:
                    _ability = ability
                    pos = worker
                    # flags[worker - 1] = False
                    # ret += ability
                    # break
            if pos != -1:
                flags[pos] = False
                ret += _ability
    return ret

if __name__ == "__main__":
    m, n = list(map(int, input().split(" ")))
    workers = []
    for i in range(n):
        workers.append(list(map(int, input().split(" "))))
    print(max_ability(m, workers))



            
        






