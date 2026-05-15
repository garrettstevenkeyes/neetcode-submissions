class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            midRow = (top+bottom)//2
            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bottom = midRow - 1
            else:
                break

        if not (top <= bottom):
            return False

        s,e = 0,len(matrix[midRow])-1
        while s <= e:
            mid = s + ((e-s) // 2)
            if matrix[midRow][mid] > target:
                e = mid - 1
            elif matrix[midRow][mid] < target:
                s = mid + 1
            else:
                return True
        return False
