class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a map of the courses to pre-reqs
        crsMap = {}
        for i in range(numCourses):
            crsMap[i] = []

        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        res = []
        seen = set()      # fully processed courses
        visiting = set()  # courses in current dfs path

        def dfs(crs):
            # cycle
            if crs in visiting:
                return False
            # already processed
            if crs in seen:
                return True

            visiting.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            seen.add(crs)
            res.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res