#AAABABB
# s
#    e
#k = 0
#seen = {}

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        start = 0
        end = 0
        res = 0
        while end < len(s):
            seen[s[end]] = seen.get(s[end], 0) + 1

            while end - start + 1 - max(seen.values()) > k:
                seen[s[start]] -= 1
                start += 1

            res = max(res, end - start + 1)
            end += 1
        
        return res