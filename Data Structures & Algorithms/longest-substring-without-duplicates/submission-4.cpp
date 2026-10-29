class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int counter = 0;
        int j = 0;
        int size;
        unordered_map<char,int> hashmap;

        for(int i=0;i<s.size();i++){
            char lettre = s[i];
            hashmap[lettre]++;
            while (hashmap[lettre]>=2){
                hashmap[s[j]]--;
                j++;
            }
            size = i-j+1;
            counter = max(counter,size);
            
        }
        return counter;
        
    }
};
