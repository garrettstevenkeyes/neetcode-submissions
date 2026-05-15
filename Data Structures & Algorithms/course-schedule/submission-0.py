class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create map of course to prereqs
        #is course initially has an empty list or prereqs as values
        preMap = { i:[] for i in range(numCourses)}
        #iterate prereqs and save to each course
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        #visitSet for all courses on the DFS path
        visitSet = set()
        def dfs(crs):
            #if we are visiting a course already
            #then we are in a loop and return false
            if crs in visitSet:
                return False

            #if the course has no prereqs
            #then we can return true
            if preMap[crs] == []:
                return True

            #add our visited item to the set
            visitSet.add(crs)
            #look at the prereqs for the course
            for pre in preMap[crs]:
                #if it returns false then we reutrn false
                if not dfs(pre): return False 
            #then we can remove our course from the visitSet
            visitSet.remove(crs)
            #and set our premap to an empty list 
            #so if we visit it again we dont have to do repeat work
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True