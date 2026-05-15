#brainstorm
#   [1,2,3],   [7,4,1].  (0,0)-> (2,2)
#   [4,5,6], ->[8,5,2].  
#   [7,8,9].   [9,6,3]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            #iterate through row except right element
            for i in range(r - l):
                top, bottom = l, r

                #save the top left value
                topLeft = matrix[top][l + i]
                #move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                #move the bottom right into the bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                #move the top right into the bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                #move the saved top left to the top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1
        