#include <algorithm>

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        
        priority_queue<int> q;
        for ( int i = 0; i< stones.size();i++){
            q.push(stones[i]);
        };

        while(q.size()>=2){
            int first = q.top();
            q.pop();
            int second = q.top();
            q.pop();
            if (first<second) q.push(second-first);
            if (first>second) q.push(first-second);
            if (first==second) q.push(0);
        }
        return q.top();
    }
};
