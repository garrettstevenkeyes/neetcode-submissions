class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        #add stones to the heap
        #make neg for max heap
        heapq.heapify(stones)
        #while there are more than 1 stones present
        while len(stones) > 1:
            #if there are two stones left
            #smash stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first < second:
                #add to heap
                heapq.heappush(stones, first - second)
        #if stones is empty
        stones.append(0)
        return abs(stones[0])


