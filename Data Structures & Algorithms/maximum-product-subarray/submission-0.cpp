class Solution {
public:
    int maxProduct(vector<int>& nums) {
        //dp[i] , largest product with subbaray of size i 
        int n = nums.size();
        int currmax = nums[0];
        int currmin = nums[0];
        int res = nums[0];
        
        for ( int i  = 1 ; i<n ; i++){
            int x = nums[i];
            if (x<0) swap(currmax,currmin);
            currmax = max(x,currmax*x);
            currmin = min(x,currmin*x);
            res = max(currmax,res);
        };

        return res;
    }
};
