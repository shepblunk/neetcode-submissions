class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int> hashmap;
        for ( int i = 0 ; i < nums.size(); i++){
            if (hashmap.contains(nums[i])) return nums[i];
            else hashmap[nums[i]]++;
        }
        
    }
};
