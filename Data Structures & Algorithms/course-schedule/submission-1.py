class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create map of courses
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #used for cycle detection
        visitSet = set()
        def dfs(crs):
            #base case cycle
            if crs in visitSet:
                #then its a cycle
                return False
            
            #if no prereqs
            if not preMap[crs]:
                return True

            #add visited
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        #call dfs for every crs
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True