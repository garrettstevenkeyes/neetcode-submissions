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

        for (int i = 0; i < s.size(); i++){
            if (myMap.find(s[i]) != myMap.end()){
                if (!myStack.empty() && myStack.top() == myMap[s[i]]){
                    myStack.pop();
                } else {
                    return false;
                }
            } else {
                myStack.push(s[i]);
            }
        }

        return myStack.empty();
    }
};


// 