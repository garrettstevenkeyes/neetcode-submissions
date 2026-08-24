class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        midRowIdx = 0
        startRowIdx, endRowIdx = 0, len(matrix) - 1
        while startRowIdx <= endRowIdx:
            midRowIdx = (startRowIdx + endRowIdx) // 2
            if matrix[midRowIdx][-1] < target:
                startRowIdx = midRowIdx + 1
            elif matrix[midRowIdx][0] > target:
                endRowIdx = midRowIdx - 1
            else:
                break
        
        if not (startRowIdx <= endRowIdx):
            return False
        
        row = matrix[midRowIdx]
        startColIdx, endColIdx = 0, len(row) - 1
        while startColIdx <= endColIdx:
            mid = (startColIdx + endColIdx) // 2
            if row[mid] > target:
                endColIdx = mid -1
            elif row[mid] < target:
                startColIdx = mid + 1
            else:
                return True
        return False