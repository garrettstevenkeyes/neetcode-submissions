#include <vector>

class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";
        for (auto str : strs){
            encodedString += to_string(str.size()) + "#" + str;
        }
        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> strVec;
        int i = 0;

        while (i < s.length()) {
            // Find the position of the next '#' from position i
            int j = s.find('#', i);
            // Get the length of the next string
            int length = stoi(s.substr(i, j - i));
            // Move `i` past the length and '#'
            i = j + 1;
            // Extract the string using the length
            strVec.push_back(s.substr(i, length));
            // Move `i` to the next starting position
            i += length;
        }
        return strVec;
    }
};
