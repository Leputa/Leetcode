class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        idx = -1
        remain = 0
        for i in range(len(gas)):
            remain += (gas[i] - cost[i])
            if remain < 0:
                idx = i + 1
                remain = 0
        return idx