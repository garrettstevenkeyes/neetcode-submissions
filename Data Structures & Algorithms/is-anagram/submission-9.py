class Solution:
    #time O(N)
    #space (N)
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        #could chars in list
        for char in list(s):
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1

        #iterate other word
        for char in list(t):
            if char not in seen:
                return False
            elif seen[char] == 1:
                del seen[char]
            else:
                seen[char] -= 1
        
        return True if not seen else False
        