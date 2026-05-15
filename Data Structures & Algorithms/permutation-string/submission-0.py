#brainstorm
# lecabee
# i
#   j
# abc
#
#planning

#implementation

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        window_size = len(s1)

        for i in range(len(s2) - window_size + 1):
            window = s2[i:i + window_size]
            window_count = Counter(window)
            if window_count == s1_count:
                return True
        return False