class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        week, month = 0, 0
        dp = [0] * (len(days) + 1)
        for i in range(len(days)):
            while days[week] < days[i] - 6:
                week += 1
            while days[month] < days[i] - 29:
                month += 1
            dp[i+1] = min(dp[i] + costs[0], dp[week] + costs[1], dp[month] + costs[2])
        return dp[len(days)]