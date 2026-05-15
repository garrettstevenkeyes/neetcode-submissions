class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        // define res vars
        var res: [Int] = Array(repeating: 1, count: nums.count)
        var prefix = 1
        for idx in (0..<nums.count) {
            res[idx] = res[idx] * prefix
            prefix = nums[idx] * prefix
        }

        var postfix = 1
        for idx in (0..<nums.count).reversed(){
            res[idx] = res[idx] * postfix
            postfix = nums[idx] * postfix
        }

        return res
    }
}
