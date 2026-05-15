class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #create list of empty arrays equal to list of num length
        freq = [[] for i in range(len(nums) +1)]

        #for each number
        #add 1 to the count of that number
        #in our dict
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        #for each count add the number 
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




