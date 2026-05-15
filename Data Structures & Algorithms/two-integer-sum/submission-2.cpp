#include <unordered_map>
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> myMap;
        std::vector<int> myList;

        for (int i = 0; i < nums.size(); i++){
            if (myMap.find(nums[i]) != myMap.end()){
                myList.push_back(myMap[nums[i]]);
                myList.push_back(i);
                return myList;
            } else {
                int newVal = target - nums[i];
                myMap[newVal] = i;
            }
        }

        return myList; 
    }
};
