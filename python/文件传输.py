def max_file_num(t, n):
    files = zip(t, n)
    files = sorted(files, key = lambda x: x[0])
    t = [file[0] for file in files]
    n = [file[1] for file in files]

    max_num = 0
    nums = 0

    for i in range(len(t)):
        if i > 0:
            delta_t = t[i] - t[i-1]
            nums = max(0, nums-delta_t)

        nums += n[i]
        if nums > max_num:
            max_num = nums

        if i == len(t) - 1:
            times = t[i] + nums

    print(times, max_num)


if __name__ == "__main__":
    n = int(input())
    t, c = [], []
    for i in range(n):
        line = list(map(int, input().split(" ")))
        t.append(line[0])
        c.append(line[1])

    max_file_num(t, c)
    # max_file_num([1, 2, 3], [3, 3, 3])





