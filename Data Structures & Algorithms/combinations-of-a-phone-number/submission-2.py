class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if there are no digits return 
        if len(digits) == 0:
            return []

        res = []
        #define dfs func, takes subset and idx
        def dfs(subset, idx):
            #base case if idx == len digits add to res and return
            if idx == len(digits):
                res.append("".join(subset))
                return
            
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

            #iterate through letters of number
            for letter in numMap[digits[idx]]:
                #add to subset
                subset.append(letter)
                #recurse 
                dfs(subset, idx + 1)
                #remove from subset
                subset.pop()

        dfs([], 0)
        return res


        