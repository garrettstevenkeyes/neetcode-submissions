class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var dupDict: [Int : Int] = [:]
        for num in nums {
            if (dupDict[num] != nil){
                return true
            } else {
                dupDict[num] = 1
            }
        }
        return false
    }
}
