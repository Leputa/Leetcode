# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals

        ret = []
        intervals = sorted(intervals, key = lambda x: x.start)
        tmp_interval = Interval(intervals[0].start, intervals[0].end)

        for i in range(1, len(intervals)):
            this_start = intervals[i].start
            this_end = intervals[i].end
            if this_start <= tmp_interval:
                tmp_interval.end = this_end
                if i == len(intervals) - 1:
                    ret.append(tmp_interval)
            else:
                ret.append(tmp_interval)
                tmp_interval = Interval(intervals[i].start, intervals[i].end)

        return ret
            




if __name__ == '__main__':
    intervals = [Interval(1, 3), Interval(0, 6), Interval(8, 10), Interval(15, 18)]
    print(Solution().merge(intervals))