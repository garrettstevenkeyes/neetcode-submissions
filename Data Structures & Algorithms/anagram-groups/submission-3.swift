// #Plans
// #1. create result dictionary where keys with will ascii list and values are a list
// #2. iterate through strings
// #3. count ord value of chars
// #4. save the dict
// #5. return dict values
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        // #1. create result dictionary where keys with will ascii list and values are a list
        var res : [[Int]: [String]] = [:]
        // #2. iterate through strings
        for string in strs {
            // #3. count ord value of chars
            var charsCounts = Array(repeating: 0, count:26)
            for char in string {
                let charVal = Int(char.asciiValue! - Character("a").asciiValue!)
                charsCounts[charVal] += 1
            }
            // #4. save the dict
            res[charsCounts, default:[]].append(string)
        }
        
        
        // #5. return dict values
        return Array(res.values)
    }
}
