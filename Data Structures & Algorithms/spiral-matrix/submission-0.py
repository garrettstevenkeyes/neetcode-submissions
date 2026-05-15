#Brainstorm
# Time  O(MxN)
# Space O(N) for new output data structure
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #define res structure
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #get top row
            for col_idx in range(left,right):
                res.append(matrix[top][col_idx])
            #move top down
            top += 1

            #get right side
            for row_idx in range(top, bottom):
                #right - 1 for idx
                res.append(matrix[row_idx][right-1])
            right -= 1

            #check for a violation mid way
            if not (left < right and top < bottom):
                break

            #get bottom
            #right -1 for idx , left -1 for idx, in reverse
            for col_idx in range(right -1, left-1, -1):
                res.append(matrix[bottom-1][col_idx])
            bottom -= 1

            #get left
            #
            for row_idx in range(bottom-1,top-1, -1):
                res.append(matrix[row_idx][left])
            left += 1
        
        return res
