class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        #turn nums into min heap
        heapq.heapify(self.minHeap)
        #while it is larger than what we need pop
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #push item onto the heap
        heapq.heappush(self.minHeap, val)
        #but we want it to be of size k
        #so pop while its larger than that
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
