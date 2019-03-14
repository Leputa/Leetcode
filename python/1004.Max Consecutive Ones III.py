import queue

class Solution:
    def longestOnes(self, A, K):
        max_cnt = 0
        cnt = 0
        idx_queue = queue.Queue()
        for i in range(len(A)):
            if A[i] == 1:
                cnt += 1
            else:
                if K > 0:
                    idx_queue.put(i)
                    K -= 1
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt 
                else:
                    if cnt > max_cnt:
                        max_cnt = cnt
                    idx_queue.put(i)
                    pre_change_idx = idx_queue.get()
                    cnt = i - pre_change_idx
        return max_cnt

if __name__ == "__main__":
    print(Solution().longestOnes([0,0,1,1,1,0,0], 0))
                        

                 