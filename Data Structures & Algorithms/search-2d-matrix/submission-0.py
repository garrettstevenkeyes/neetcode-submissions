class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        def binarySearch(row, target):
            s,e = 0,len(row)-1
            while s <= e:
                mid = s + ((e-s) // 2)
                if row[mid] > target:
                    e = mid - 1
                elif row[mid] < target:
                    s = mid + 1
                else:
                    return True
            return False

        for r in matrix:
            if binarySearch(r, target) == True:
                return True

        return False
        
