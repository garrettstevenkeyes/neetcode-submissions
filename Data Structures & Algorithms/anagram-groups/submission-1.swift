class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        // define dict where keys are character counts
        var res: [[Int]: [String]] = [:]

        // values are arrays of strings
        for s in strs {
            // create empty letter count array
            var count = Array(repeating:0, count:26)

            // count chars in the string
            for c in s {
                // get char position
                let index = Int(c.asciiValue! - Character("a").asciiValue!)
                count[index] += 1
            }

            res[count, default: []].append(s)
        }

        return Array(res.values)
    }
}
