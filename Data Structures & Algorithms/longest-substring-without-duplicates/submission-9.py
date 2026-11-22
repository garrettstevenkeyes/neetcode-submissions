#zxyzxyz
# s
#   e

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        res = 0
        seen = set()
        start = 0
        end = 0
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                res = max(res, end-start+1)
                end += 1
            else:
                seen.remove(s[start])
                start += 1
            
        return res

        
        