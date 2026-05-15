class Solution {
    func jump(_ nums: [Int]) -> Int {
        // # init a right and left
        var left = 0
        var right = 0
        // # init res
        var res = 0
        // #iterative right pointer
        // #until we reach the end
        while (right < nums.count-1) {
            //     #define the longest jump as 0 to start
            var longestJump = 0
            //     #get the furthest jump
            for i in left..<right+1 {
                longestJump = max(longestJump, nums[i])
            }
            //     #move left 1 past right
            left = right + 1
            
            //     #move right to current + longest
            right += longestJump
            //     # add one to the minimum jumps
            res += 1
        }
        
        
        return res
    }
}
