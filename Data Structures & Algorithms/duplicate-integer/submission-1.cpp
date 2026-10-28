class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> hm;
        for(int i =0 ;i<nums.size();i++){
            hm[nums[i]]++;
            if (hm[nums[i]]>=2) return true;
        }
    return false;
        
    }
};