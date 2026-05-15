class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort first so the candidates are in order
        candidates.sort()
        res = []

        def dfs(start, subSeq):
            #if our sum equals our target
            if sum(subSeq)==target:
                res.append(subSeq.copy())
                return 
            #if our index is out of range of the list 
            #or if our total is over the target
            #return
            if sum(subSeq) > target:
                return 

            #otherwise check if our numbers are the same
            #skip because we want unique

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
            
                #do combination
                subSeq.append(candidates[i])
                dfs(i+1, subSeq)

                #remove and do other option
                subSeq.pop()
            
        dfs(0,[])
        return res