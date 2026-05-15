class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var seen = Set<Character>()
        var left = 0
        var maxLength = 0
        let chars = Array(s)  // Convert to array for indexing
        
        for right in 0..<chars.count {
            // Shrink from left while duplicate exists
            while seen.contains(chars[right]) {
                seen.remove(chars[left])
                left += 1
            }
            
            seen.insert(chars[right])
            maxLength = max(maxLength, right - left + 1)
        }
        
        return maxLength
    }
}
