class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[6,7],[1,3],[1,5]]

        if len(intervals) <= 1:
            return intervals

        #sort lists by the first item
        intervals.sort(key=lambda x: x[0])

        i = 1
        while i < len(intervals):
            # compare first item in list
            # if second space greater than first in second item merge
            if (intervals[i][0] >= intervals[i-1][0]) and (intervals[i][0] <= intervals[i-1][1]):
                newInterval = [intervals[i-1][0], max(intervals[i][1], intervals[i-1][1])]
                intervals[i-1] = newInterval
                intervals.pop(i)
            else:
                i += 1
        return intervals

