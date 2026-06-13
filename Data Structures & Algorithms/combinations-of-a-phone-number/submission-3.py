class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #dictionary with number to letter pairings
        numMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        #if there are no digits return nothing
        if len(digits) == 0: return []
        #init res
        res = []
        def dfs(i, path):
            # if path is complete, add it
            if len(path) == len(digits):
                res.append(path)
                return
            # only look at the current digit
            num = digits[i]
            # try each possible letter for this digit
            for letter in numMap[num]:
                dfs(i + 1, path + letter)
        dfs(0, "")
        return res