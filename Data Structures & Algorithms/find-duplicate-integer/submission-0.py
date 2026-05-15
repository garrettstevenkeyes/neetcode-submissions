class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #detect the cycle
        slow, fast = 0, 0
        while True:
            #iterate through the list
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #find the duplicate
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow