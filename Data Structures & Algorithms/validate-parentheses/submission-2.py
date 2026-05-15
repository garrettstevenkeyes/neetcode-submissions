class Solution:
    def isValid(self, s: str) -> bool:
        matchingPairs = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif c not in matchingPairs:
                stack.append(c)
            elif stack[-1] != matchingPairs[c]:
                stack.append(c)
            else:
                stack.pop()
        
        return len(stack)==0