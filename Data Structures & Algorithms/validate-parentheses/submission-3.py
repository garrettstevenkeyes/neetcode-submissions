class Solution:
    def isValid(self, s: str) -> bool:
        #([{}])
        #     i
        #[]
        #init res stack
        #init dict with pairings
        lookupPairings = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        res = []

        for char in s:
            #if its a close do lookup
            #if the res list is empty its invalid
            if char in lookupPairings:
                #exit condition
                if len(res) == 0:
                    return False
                
                #check end of stack and pop
                if res[-1] == lookupPairings[char]:
                    res.pop()
                else:
                    return False

            else:
                res.append(char)
        
        return len(res) == 0

