class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create empty dict items for no pre rec courses
        course_catalog = {i:[] for i in range(numCourses)}
        #iterate the courses and save them to a dict
        for crs, pre in prerequisites:
            course_catalog[crs].append(pre)
        
        seen = set()
        #do a second iteration via dfs on the courses
        def dfs(course):
            #base case cycle
            if course in seen:
                return False
            # if a course has no prerecs return true
            if not course_catalog[course]:
                return True

            #add to seen
            seen.add(course)
            for pre in course_catalog[course]:
                if not dfs(pre): return False

            #after you check a course mark it as possible if it is
            #by erasing prerecs
            seen.remove(course)
            course_catalog[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True



