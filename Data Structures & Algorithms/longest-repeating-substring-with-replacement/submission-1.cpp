class Solution {
public:
    int characterReplacement(string s, int k) {

        int i = 0;
        int counter = 0;
        int maxFreq = 0;

        unordered_map<char,int> hashmap;

        for(int r = 0; r < s.size(); r++) {

            hashmap[s[r]]++;

            maxFreq = max(maxFreq, hashmap[s[r]]);

            while ((r-i+1) - maxFreq > k) {
                hashmap[s[i]]--;
                i++;
            }

            counter = max(counter, r-i+1);
        }

        return counter;
    }
};