from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips, key=lambda info: info[0])
        dp = [float("inf")] * (max(T + 1, max([clip[1] for clip in clips])) + 1)
        for i in range(len(clips)):
            if clips[i][0] == 0:
                for j in range(clips[i][1] + 1):
                    dp[j] = 1
            else:
                for j in range(clips[i][0], clips[i][1]):
                    dp[clips[i][1]] = min(dp[clips[i][1]], dp[j] + 1)
                    dp[j] = min(dp[j], dp[clips[i][1]])
        if dp[T] == float("inf"):
            return - 1
        else:
            return dp[T]



if __name__ == "__main__":
    print(Solution().videoStitching([[0,4],[2,8]], 5))
