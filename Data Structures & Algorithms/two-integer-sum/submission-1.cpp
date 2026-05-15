#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> myMap;

        for (int i=0; i < nums.size(); i++){
            int compliment = target - nums[i];

            if(myMap.find(compliment) != myMap.end()){
                return std::vector<int>{myMap[compliment], i};
            } 
            
            myMap[nums[i]] = i;   
        }

        return std::vector<int>{};
    }
};
