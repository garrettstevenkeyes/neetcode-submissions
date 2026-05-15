class Solution {
    func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
        // """
        // gas = [1,2,3,4], cost = [2,2,4,1]
        //        i
        //       []

        // 1. if you have more cost than gas it cant be done
        // 2. for each space if it cost more than gas move the res
        // 3. return the result
        // """
        if gas.reduce(0, +) < cost.reduce(0, +) {
            return -1
        }
        var res = 0
        var total = 0
        for i in gas.indices {
            total += gas[i] - cost[i]
            if total < 0 {
                total = 0
                res = i + 1
            }
        }
        return res
    }
}
