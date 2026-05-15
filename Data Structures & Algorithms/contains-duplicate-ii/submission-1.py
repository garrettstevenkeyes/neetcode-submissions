class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            #if the window is outside of the range
            #remove the numer and increase the range
            if R - L > k:
                window.remove(nums[L])
                L += 1
            #if there is a match return true
            if nums[R] in window:
                return True
            #otherwise add to the window
            window.add(nums[R])
        #return false if you passed through the window
        return False

