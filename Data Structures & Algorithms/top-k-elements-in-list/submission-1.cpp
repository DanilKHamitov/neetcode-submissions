class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        vector<vector<int>> freq(nums.size()+1);
        for(int i =0;i<nums.size();++i)  {
            cnt[nums[i]]++;
        }
        for(const auto &emp : cnt ) {
            freq[emp.second].push_back(emp.first);
        }
        vector<int> res;
        for(int i=freq.size()-1;i>0;--i) {
           for(int n : freq[i]) {
            res.push_back(n);
            if(res.size()==k) {
                return res;
            }
           }
        }
        return res;
    }
};
