// #Plan
// #1. create empty dict
// #2. iterate the list
// #3. get compliment by doing target - num 
// #4. if compliment is in dict return [compliment, curIdx]
// #5. else save compliment
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        // #1. create empty dict
        var numIdxDict : [Int: Int] = [:]
        // #2. iterate the list
        for (idx, num) in nums.enumerated(){
            // #3. get compliment by doing target - num 
            var compliment = target - num

            // #4. if compliment is in dict return [compliment, curIdx]
            if let complimentIdx = numIdxDict[compliment] {
                return [complimentIdx, idx]
            }
            // #5. else save compliment
            numIdxDict[num] = idx
        }
        return []
    }
}
