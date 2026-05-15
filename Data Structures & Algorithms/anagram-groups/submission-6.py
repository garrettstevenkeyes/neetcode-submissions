# Brainstorm
# Time O(N x M)
# Space O(N)

# Plan
# 1. define result dict where key is ascii value of word, value is list of words
# 2. iterate over string list
# 2.5 create 26char list of 0's
# 3. for each char in the list get the ascii value and add it to list
# 4. return the dict values as a list
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. define result dict where key is ascii value of word, value is list of words
        res = defaultdict(list)
        # 2. iterate over string list
        for word in strs:
            # 2.5 create 26char list of 0's
            charList = [0] * 26
            for char in word:
                ordCharVal = ord(char) - ord('a')
                charList[ordCharVal] += 1
            # 3. for each char in the list get the ascii value and add it to list
            res[tuple(charList)].append(word)
        # 4. return the dict values as a list
        return list(res.values())