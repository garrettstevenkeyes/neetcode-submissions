class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        charDict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def combinations(i, subset):
            if i == len(digits):
                res.append("".join(subset))
                return
            
            for char in charDict[digits[i]]:
                subset.append(char)
                combinations(i + 1, subset)
                subset.pop()

        combinations(0,[])
        return res
        



