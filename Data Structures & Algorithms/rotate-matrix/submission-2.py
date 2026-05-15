#Brainstorm
#Time O(N^2)
#Space O(1)

#Plan
#create l,r pointers looking at start and end of list
#define top, bottom 
#save upper left into tmp
#replace upper right with upper left
#replace bottom right with upper right
#replace bottom left with bottom right
#replace upper left with bottom left
#move pointers in
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #create l,r pointers looking at start and end of list
        l,r = 0, len(matrix)-1
        while l < r:
            #loop through row
            for i in range(r-l):
                #define top, bottom 
                top, bottom = l, r

                #save upper left into tmp
                topLeft = matrix[top][l+i]
                #replace upper left with bottom left
                matrix[top][l+i] = matrix[bottom-i][l]
                #replace bottom left with bottom right
                matrix[bottom-i][l] = matrix[bottom][r-i]
                #replace bottom right with upper right
                matrix[bottom][r-i] = matrix[top+i][r]
                #replace upper right with upper left
                matrix[top+i][r] = topLeft
                
            #move pointers in
            l += 1
            r -= 1