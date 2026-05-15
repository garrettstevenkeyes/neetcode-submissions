# Input: matrix = [
#   [1,2,3],
#   [4,0,5],
#   [6,7,8]
#.   
# ]. l, r = 0 ,3

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #create two lists of false, for rows and cols
        #these lists represent 'does this row or col have a 0?'
        ROWS = [False] * len(matrix)
        COLS = [False] * len(matrix[0])
        #loop through the grid and if that spot equals 0 mark that 
        #row and col as having a 0
        for r in range(len(ROWS)):
            for c in range(len(COLS)):
                if matrix[r][c]==0:
                    ROWS[r] = True
                    COLS[c] = True
        #loop through again and if the number at the row or col is 0
        # mark it as a 0
        for r in range(len(ROWS)):
            for c in range(len(COLS)):
                if ROWS[r] or COLS[c]:
                    matrix[r][c] = 0

        