class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var res: [Int: Int] = [:]
        for num in nums {
            res[num, default: 0] += 1
        }

        // 2. Sort by frequency (descending) and take top k keys
        let sortedItems = res.sorted { $0.value > $1.value }
        return sortedItems.prefix(k).map { $0.key }
    }
}
