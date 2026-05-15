class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        // if the counts arnt equal return false
        if s.count != t.count { return false }
        // character dict
        var letterCounts: [Character: Int] = [:]
        // for each letter in the 
        for letter in s {
            letterCounts[letter, default: 0] += 1
        }
        
        for letter in t {
            letterCounts[letter, default: 0] -= 1
        }
        
        return letterCounts.allSatisfy { $0.value == 0 }
    }
}
