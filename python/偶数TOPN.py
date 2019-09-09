import sys

import heapq


def topN(inputs, k):
    jishu = [a for a in inputs if a % 2 == 1]
    oushu = [a for a in inputs if a % 2 == 0]
    if len(oushu) >= k:
        return sorted(oushu, reverse=True)[:k]
    else:
        return sorted(oushu, reverse=True) + sorted(jishu, reverse=True)[:k-len(oushu)]

a, b = "555503,772867,756893,339138,399447,40662,859037,628085,855723,974471,599631,636153,581541,174761,948135,411485,554033,858627,402833,546467,574367,360461,566480,755523,222921,164287,420256,40043,977167,543295,944841,917125,331763,188173,353275,175757,950417,284578,617621,546561,913416,258741,260569,630583,252845;10".split(";")
inputs = list(map(int, a.split(",")))
k = int(b)
print(topN(inputs, k))



for line in sys.stdin:
    a, b = line.split(';')
    inputs = list(map(int, a.split(",")))
    k = int(b)
    print(topN(inputs, k))
    



