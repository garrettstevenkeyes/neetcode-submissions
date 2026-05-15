class Solution {
    func jump(_ nums: [Int]) -> Int {
        // init left, right, res
        var left = 0
        var right = 0
        var res = 0
        // while right is less than the length of the list
        while right < nums.count-1 {
            // find the maximum jump you can make from left to right
            var maxJump = 0
            for i in left..<right+1 {
                maxJump = max(maxJump, i + nums[i])
            }
            // left equals one past the right
            left = right+1
            //right equals the new max distnce
            right = maxJump
            // add to our jump counter
            res += 1
        }
        // return the result
        return res
    }
}
