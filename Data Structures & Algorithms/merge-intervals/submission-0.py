class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #[[1,3],[1,5],[6,7]]
        #[]
        #sort by start time
        intervals.sort(key = lambda i: i[0])
        res = []

        #add first interval to res
        res.append(intervals[0])
        
        #iterate through the rest 
        #compare to the first one
        for interval in intervals[1:]:
            #if it starts before the last ends
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
                continue
            else:
                res.append(interval)
        
        return res

