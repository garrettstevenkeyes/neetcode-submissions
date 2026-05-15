class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        // zxyzxyz
        //     l
        //       r
        // seen set[z,x,y]

        // init left, res, and set
        var left = 0
        var res = 0
        var seen = Set<Character>()
        var chars = Array(s)

        //interate 
        for right in 0..<chars.count {
            // check if we have seen the letter
            while seen.contains(chars[right]){
                seen.remove(chars[left])
                left += 1
            }

            // insert the right char
            seen.insert(chars[right])
            res = max(res, right - left + 1)
        }

        return res
    }
}
