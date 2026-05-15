class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #define res list
        res = []
        #define left, right, top and bottom
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        #loop while the left is < right
        #while the top < bottom
        while left < right and top < bottom:
            #iterate left -> right
            # add to res
            #move top down
            for col_idx in range(left, right):
                res.append(matrix[top][col_idx])
            top += 1

            #iterate top -> bottom
            # add to res
            #move right in
            for row_idx in range(top, bottom):
                res.append(matrix[row_idx][right-1])
            right -= 1

            #check our condition
            if not (top < bottom and left < right):
                break

            #iterate right -> left
            # add to res
            #move bottom up
            for col_idx in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][col_idx])
            bottom -= 1

            #iterate bottom to top
            # add to res
            # move left in
            for row_idx in range(bottom -1, top -1, -1):
                res.append(matrix[row_idx][left])
            left += 1
        return res
