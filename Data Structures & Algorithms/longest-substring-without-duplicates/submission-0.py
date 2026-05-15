#. ()
# "zxyzxyz"
#  i
#  j

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #define result
        res = 0
        #while i is in the range of the string
        for i in range(len(s)):

            maxLength = 0
            seen = set()
            j = i
            #check whether j is in the range of the string 
            #and that the letter hasnt been seen
            while j < len(s) and s[j] not in seen:
                seen.add(s[j])
                maxLength += 1
                j += 1
            res = max(res, maxLength)
        return res


