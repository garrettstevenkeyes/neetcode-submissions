class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        #   s
        #.    e
        # seen = [xyz]
        #init s and e
        #init seen list

        #while e is not in seen keep going if it is move s until its not, 
        # pop from the front of seen

        start, end = 0, 0
        seen = []
        maxLenSeen = 0

        while end < len(s) and start <= end:
            if s[end] not in seen:
                seen.append(s[end])
                end += 1
                maxLenSeen = max(maxLenSeen, len(seen))

            else:
                seen.pop(0)
                start += 1
        
        return maxLenSeen

        

       