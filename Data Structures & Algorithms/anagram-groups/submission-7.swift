// # Plan
// # 1. define result dict where key is ascii value of word, value is list of words
// # 2. iterate over string list
// # 2.5 create 26char list of 0's
// # 3. for each char in the list get the ascii value and add it to list
// # 4. return the dict values as a list

class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        // # 1. define result dict where key is ascii value of word, value is list of words
        var res : [[Int]:[String]] = [:]
        // # 2. iterate over string list
        for word in strs {
            // # 2.5 create 26char list of 0's
            var ordCharList = Array(repeating:0, count:26)
            // # 3. for each char in the list get the ascii value and add it to list
            for char in word {
                var ordCharVal = Int(char.asciiValue! - Character("a").asciiValue!)
                ordCharList[ordCharVal] += 1
            }
            res[ordCharList, default:[]].append(word)
        }
        // # 4. return the dict values as a list
        return Array(res.values)
    }
}
