#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        std::unordered_map<char, int> myDict;

        for (auto& c : s){
            myDict[c] += 1;
        }
        
        for (auto& c : t){
            if (myDict.find(c) != myDict.end() && 
            myDict[c] - 1 >= 0){
                myDict[c] -= 1;
            } else {
                return false;
            }
        }

        return true; 
    }
};
