#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> myDict;

        for (auto& num : nums){
            myDict[num] += 1;
            if (myDict[num] > 1){
                return true;
            }
        }

        return false;
    }
};
