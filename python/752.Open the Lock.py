import queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        q = queue.Queue()
        q.put("0000")
        deadends.add("0000")    #防止回退

        down_up = [1, -1]
        turn = 0
        while (not q.empty()):
            size = q.qsize()
            for i in range(size):
                tmp_lock = q.get()
                if tmp_lock == target:
                    return turn
                for j in range(4):
                    for k in range(2):
                        pos_j = str((ord(tmp_lock[j]) - ord("0") + down_up[k] + 10) % 10)
                        new_lock = list(tmp_lock)
                        new_lock[j] = pos_j
                        new_lock = "".join(new_lock)
                        if new_lock not in deadends:
                            deadends.add(new_lock)
                            q.put(new_lock)
            turn += 1
        return -1



