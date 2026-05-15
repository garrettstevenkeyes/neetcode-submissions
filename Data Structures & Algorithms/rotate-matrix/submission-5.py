class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Define border
        l, r = 0, len(matrix) - 1
        #while within the border
        while l < r:
            # for each number in the range or the left to the right
            for i in range(r - l):
                #define the top and bottom
                #its a square so its the same as l and r
                top, bottom = l, r
                #pull the top left spot
                topLeft = matrix[top][l+i]
                #set the top left to the bottom left
                matrix[top][l+i] = matrix[bottom-i][l]
                #set the bottom left to the bottom right
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #set the bottom right to the top right
                matrix[bottom][r-i] = matrix[top+i][r]
                #set the top right to the top left
                matrix[top+i][r] = topLeft
            #move the left and right in
            l += 1
            r -= 1
        #no return because its inplace