class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create buckets
        res = []
        buckets = [[] for i in range(len(nums)+1)]
        #count the number frequency
        numCount = {}
        for n in nums:
            numCount[n] = 1 + numCount.get(n, 0)

        #distribute into buckets 
        for num, count in numCount.items():
            buckets[count].append(num)
        

        #get top k
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:

                res.append(n)
                if len(res) == k:
                    return res


