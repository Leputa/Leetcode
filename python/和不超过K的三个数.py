
global cnt


def sumLessThanK(nums, K):
    nums = sorted(nums)
    global cnt
    cnt = 0
    traceback(nums, [False] * len(nums), K, 0, 0, 0)
    return cnt


def traceback(nums, flags, K, tmpSum, c, pre_position):
    if c == 3:
        global cnt
        cnt += 1
        return 
    for i in range(pre_position, len(nums)):
        if tmpSum + nums[i] >= K:
            break 
        if flags[i] == False:
            flags[i] = True
            tmpSum += nums[i]
            c += 1
            traceback(nums, flags, K, tmpSum, c, i+1)
            c -= 1
            tmpSum -= nums[i]
            flags[i] = False


if __name__ == "__main__":
    # print(sumLessThanK([-2, 0, 1, 2, 3, 6], 2))
    n = int(input())
    nums = list(map(int, input().split(" ")))
    K = int(input())
    print(sumLessThanK(nums, K))

