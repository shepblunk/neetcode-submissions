
class Solution {
public:

    void backtrack(
        vector<int>& nums,
        int remaining,
        int start,
        vector<int>& current,
        vector<vector<int>>& result
    ) {

        if (remaining == 0) {
            result.push_back(current);
            return;
        }

        if (remaining < 0) return;

        for (int i = start; i < nums.size(); i++) {

            current.push_back(nums[i]);

            backtrack(nums, remaining - nums[i], i, current, result);

            current.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {

        vector<vector<int>> result;
        vector<int> current;

        backtrack(nums, target, 0, current, result);

        return result;
    }
};
