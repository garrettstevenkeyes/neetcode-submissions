# Brainstorm
# Time O(n)
# Space O(n)

# Plan
# 1. Create result dict, key is tuple and value is list of strings
# 2. for each word, get the ascii char counts
# 3. save it into the dictionary
# 4. return the dictionary values
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create result dict, key is tuple and value is list of strings
        res = defaultdict(list)
        # 2. for each word, get the ascii char counts
        for word in strs:
            charVals = [0] * 26
            for char in word:
                val = ord(char) - ord('a')
                charVals[val] += 1
            # 3. save it into the dictionary
            res[tuple(charVals)].append(word)
        # 4. return the dictionary values
        return list(res.values())