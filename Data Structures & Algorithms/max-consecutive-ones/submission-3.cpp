
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        
        int k=0;
        int mx = 0;
        for(int j=0;j<nums.size();++j) {
              if(nums[j] == 1) {
                ++k;
              } else { 
                    if(k >= mx) {
                         mx = k; }  
                    k = 0; }
        }
        return max(mx,k);
    }
};