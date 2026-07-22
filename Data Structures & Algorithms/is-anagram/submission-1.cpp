class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int,int> t_seen,s_seen;
        for(int i =0;i<t.size();++i) {
            t_seen[t[i]]++;
        }
        for(int i =0;i<s.size();++i) {
            s_seen[s[i]]++;
        }
    
    if (t_seen == s_seen) {
        return true;
    
    } else { 
        return false;
    }
    }
};
