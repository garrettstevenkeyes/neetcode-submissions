class Solution:
    #time O(n)
    #space O(n)
    #data structure = stack
    def isValid(self, s: str) -> bool:
        matchingPairs = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        
        seen = []

        for bracket in s:
            #if its a closing item
            if bracket in matchingPairs:
                #remove from the end of seen

                if seen and seen[-1] == matchingPairs[bracket]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(bracket)
        return len(seen) == 0


        