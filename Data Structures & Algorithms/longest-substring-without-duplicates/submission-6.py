class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a set
        seen = set()
        #use two pointers and iterate
        start, end = 0, 0
        stringList = list(s)
        res = 0
        #while the end is in the s range
        while end < len(stringList):
            #while the character at the end is in the set
            while stringList[end] in seen:
                #remove the start char from the set and increment start
                seen.remove(stringList[start])
                start += 1 
                
            #otherwise add the end character
            seen.add(stringList[end])
            #take a max length of the set
            res = max(res, len(seen))
            end += 1
        
        #return the res
        return res
