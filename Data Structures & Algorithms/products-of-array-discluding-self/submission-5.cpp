class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
    vector<int> pref(nums.size(),1),suff(nums.size(),1);//pref[i]*suff[i] = output[i]
    int prod = 1; 
    for(int i =0;i<nums.size();++i) {
        pref[i]= prod;
        prod*= nums[i];
    }
    prod = 1;
    for(int i=nums.size()-1;i>=0;--i) {
        suff[i] = prod;
        prod*= nums[i];

    }
    vector<int> output(nums.size());
    for(int i =0;i<output.size();++i) {
        output[i] = pref[i] * suff[i];
    }
    return output;
    }
};
