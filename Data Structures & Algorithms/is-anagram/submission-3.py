class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #define hashmap
        charCounter = {}
        #iterate list
        for c in s:
            #count elements
            if c in charCounter:
                charCounter[c] += 1
            else:
                charCounter[c] = 1
        
        #check the second string against first count
        for char in t:
            if char in charCounter:
                if charCounter[char] > 1:
                    charCounter[char] -= 1
                elif charCounter[char] == 1:
                    del charCounter[char]
                else:
                    #exit early
                    return False
            else:
                #exit early
                return False
        return len(charCounter.keys()) == 0

