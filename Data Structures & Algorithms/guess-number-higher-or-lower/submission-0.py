# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #to solve this we can use a binary search approach
        
        s, e = 1, n
        while s <= e:
            #pick a middle number check if its too high, low, or correct
            mid = s + ((e - s) // 2)
            #if too low move the start to mid + 1
            if guess(mid) == 1:
                s = mid + 1
            #if too high move the end to mid - 1
            elif guess(mid) == -1:
                e = mid -1
            else:
                return mid
        
