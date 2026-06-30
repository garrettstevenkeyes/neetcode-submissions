class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisMatch = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        seenStack = []
        for char in s:
            if (char in parenthesisMatch):
                if len(seenStack) == 0 or seenStack[-1] != parenthesisMatch[char]:
                    return False
                else:
                    seenStack.pop()
            else:
                seenStack.append(char)
            
        return len(seenStack) == 0
