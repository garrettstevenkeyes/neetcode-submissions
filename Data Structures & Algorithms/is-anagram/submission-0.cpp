#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> myCount;

        if (s.size() != t.size()){
            return false;
        }

        for (char c : s) {
            myCount[c] += 1;
        }

        for (char x : t){
            if (myCount.find(x) != myCount.end() && myCount[x] > 0){
                myCount[x]-=1;
            } else {
                return false;
            }
        }

        for (const auto& pair : myCount){
            if (pair.second != 0) {
                return false;
            }
        }
        return true;
    }
};
