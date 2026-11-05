class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        //dp[i] : the length of the longest strictly incrrasing subsequence till ith element
        int n = nums.size();
        vector<int> dp(n,1);
        for ( int i = 1 ; i < n ; i++){
            for (int j = 0; j<i ;j++){
                if(nums[i]>nums[j]){
                    dp[i] = max(dp[i],dp[j]+1);
                }
            }
        };
        return *max_element(dp.begin(),dp.end());
    }
};
