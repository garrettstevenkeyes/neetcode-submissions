class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        seen = []
        for char in s:
            if char in mapping:
                if not seen or seen[-1] != mapping[char]:
                    return False
                else:
                    seen.pop()
            else:
                seen.append(char)

        return True if not seen else False
