class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negNums = [-1*n for n in nums]
        heapq.heapify(negNums)
        res = float('-inf')
        for _ in range(k):
            res = heapq.heappop(negNums) * -1
        return res
