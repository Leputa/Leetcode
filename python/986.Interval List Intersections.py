# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def is_contain(self, A: Interval, B: Interval) -> bool:
        if A.start >= B.start and A.end <= B.end:
            return True
        else:
            return False

    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        ret = []
        idx_A, idx_B = 0, 0
        while(idx_A < len(A) and idx_B < len(B)):
            inter_A = A[idx_A]
            inter_B = B[idx_B]
            if self.is_contain(inter_A, inter_B):
                ret.append(inter_A)
                idx_A += 1
            elif self.is_contain(inter_B, inter_A):
                ret.append(inter_B)
                idx_B += 1
            else:
                # no intersection
                if inter_A.end < inter_B.start:
                    idx_A += 1
                elif inter_B.end < inter_A.start:
                    idx_B += 1
                elif inter_A.start < inter_B.start and inter_A.end >= inter_B.start:  #A前B后
                    ret.append(Interval(inter_B.start, inter_A.end))
                    idx_A += 1
                elif inter_B.start < inter_A.start and inter_B.end >= inter_A.start:
                    ret.append(Interval(inter_A.start, inter_B.end))
                    idx_B += 1

        return ret


            
