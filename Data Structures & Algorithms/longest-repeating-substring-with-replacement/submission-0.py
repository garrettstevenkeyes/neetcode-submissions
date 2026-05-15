#brainstorm
# XYYX, k=2
# i
#  j
# x = 0, y = 0
# maxL = 0
# for each char (i), j equals i. 
# while j == i or the number of subs allowed >0
# take max and continue  

#plan
#1) deplare resmax of 0
#2) loop through each char
#.  set a currentcount
#3) create a window, so while the next one is equal
#   or you have substitutions left you increment by 1
#4) when its not equal and you dont have substitutions left
#   compare the max and the current count for a new max

#implement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        #for each letter in the window
        for r in range(len(s)):
            #add one to the count if it exists
            #otherwise it has a count of 0
            count[s[r]] = 1 + count.get(s[r], 0)

            #while the size of the window - the max value count is greater than k
            #that means you need to replace too many items
            while (r - l + 1) - max(count.values()) > k:
                #so move the left pointer and remove that item from the count 
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res




#test
#XYYX, k=2
#AAABABB, k=1