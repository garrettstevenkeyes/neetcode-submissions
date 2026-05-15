// #Plan
// # 1. create two pointers on each end of the container
// # 1.5 get max value
// # 2. Compare the heights of the pillars, whichever is smaller move in
// #  because we want to look for max height
// #2.5 get max value again
// # 3. do this until the pointers are equal and return the max

class Solution {
    func maxArea(_ heights: [Int]) -> Int {
        // # 1. create two pointers on each end of the container
        var start = 0
        var end = heights.count - 1
        // # 1.5 get max value
        var maxVolume = 0
        while (start < end){
            // # 2. Compare the heights of the pillars, whichever is smaller move in
            // #  because we want to look for max height
            var volume = min(heights[start], heights[end]) * (end - start)
            maxVolume = max(maxVolume, volume)

            if (heights[start] <= heights[end]){
                start += 1
            } else {
                end -= 1
            }
        }
        return maxVolume

        
        // #2.5 get max value again
        // # 3. do this until the pointers are equal and return the max
    }
}
