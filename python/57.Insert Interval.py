# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def biSearch(key, intervals, low, high):
            # return: intervals[mid] >= key
            # 在偏右边一个位置
            while (low <= high):
                mid = (low + high) // 2
                if intervals[mid].start > key:
                    high = mid - 1
                else:
                    low = mid + 1
            return low


        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        # intervals = sorted(intervals, key = lambda x: x.start) # the intervals were initially sorted according to their start times.
        start = newInterval.start
        end = newInterval.end

        left = biSearch(start, intervals, 0, len(intervals)-1)
        right = biSearch(end, intervals, 0, len(intervals)-1)

        if left > 0 and intervals[left - 1].end >= start:
            left -= 1
            start = intervals[left].start
        if right > 0 and intervals[right - 1].end > end:
            end = intervals[right - 1].end

        intervals[left:right] = [Interval(start, end)]
        return intervals




