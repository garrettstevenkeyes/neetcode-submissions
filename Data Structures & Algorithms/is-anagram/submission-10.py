class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t: return False

        #if they are not the same len return
        if len(s) != len(t): return False

        #if the counts dont align return False
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1

        for j in range(len(t)):
            if t[j] not in chars: return False
            else: 
                if chars[t[j]] > 1:
                    chars[t[j]] -= 1
                else:
                    del chars[t[j]]
        
        return True
