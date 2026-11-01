class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        priority_queue<pair<int,int>> maxHeap;
        unordered_map<int,int> hashmap;

        for ( int i = 0; i < nums.size() ; i++){
            hashmap[nums[i]]++;
        }

        for (auto& p : hashmap){
            maxHeap.push({p.second,p.first});
        }

        vector<int> result;
        while(k>0){
            result.push_back(maxHeap.top().second);
            maxHeap.pop();
            k--;
        };

        return result;

        
    }
};
