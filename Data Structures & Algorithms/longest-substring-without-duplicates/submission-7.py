class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #zxyzxyz
        # s
        #   e
        #res = 3
        #seen = [x,y]
        seen = set()
        res = 0
        start, end = 0,0
        while end < len(s):
            if s[end] in seen:
                while s[end] in seen and start < end:
                    seen.remove(s[start])
                    start += 1 
            else:
                seen.add(s[end])
                res = max(res, end - start + 1)
                end += 1
        return res