#include <algorithm>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1, maxProfit = 0;

        while (r < prices.size()){
            if (prices[l] < prices[r]){
                int profit = prices[r] - prices[l];
                maxProfit = std::max(maxProfit, profit);
            } else {
                l = r;
            }
            r++;
        }
        return maxProfit;
    }
};


// [10,1,5,6,7,1]
//             l
//                r
//  6