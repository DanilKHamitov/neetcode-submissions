class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        int res =0;
        unordered_map<char,int> seen;
        for(int r=0;r<s.size();++r) {
            seen[s[r]]++;
            int maxFreq = max(maxFreq,seen[s[r]]);
            while( r-l + 1 - maxFreq > k) {
                seen[s[l]]--;
                ++l;
                
            }
            res= max(r-l+1,res);
        }
       return res;
    }
};
