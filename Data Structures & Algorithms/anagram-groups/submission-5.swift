// # 1. Create result dict, key is tuple and value is list of strings
// # 2. for each word, get the ascii char counts
// # 3. save it into the dictionary
// # 4. return the dictionary values
class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        // # 1. Create result dict, key is tuple and value is list of strings
        var res : [[Int]: [String]] = [:]
        // # 2. for each word, get the ascii char counts
        for word in strs {
            var charArray = Array(repeating:0, count:26)
            for char in word {
                var val = Int(char.asciiValue! - Character("a").asciiValue!)
                charArray[val] += 1
            }
            res[charArray, default: []].append(word)
        }

        return Array(res.values)
    }
}
