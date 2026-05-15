#include <unordered_map>
#include <stack>
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> myStack;
        std::unordered_map<char, char> myMap;

        myMap['}'] = '{';
        myMap[')'] = '(';
        myMap[']'] = '[';

        for (const auto& c : s){
            if (myMap.find(c) != myMap.end()){
                if (!myStack.empty() && myStack.top() == myMap[c]){
                    myStack.pop();
                } else {
                    return false;
                }
            } else {
                myStack.push(c);
            }
        }

        return myStack.empty();
    }
};


// 