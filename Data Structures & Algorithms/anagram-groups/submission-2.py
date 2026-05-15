#Brainstorm 
# Time O(N)
# Space O(N)
from collections import defaultdict

#Plans
#1. create result dictionary where keys with will ascii list and values are a list
#2. iterate through strings
#3. count ord value of chars
#4. return dict values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1. create result dictionary where keys with will ascii list and values are a list
        res = defaultdict(list)
        #2. iterate through strings
        for string in strs:
            #3. count ord value of chars
            strList = [0] * 26
            for c in string:
                val = ord(c) - ord('a')
                strList[val] += 1
            
            #4. save to dict
            res[tuple(strList)].append(string)
        #5. return dict values
        return list(res.values())
