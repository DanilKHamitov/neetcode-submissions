class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int last_ind = 0;
        for(int i =0;i<nums.size();++i) {
            if (nums[i] != val) {
                nums[last_ind] = nums[i];
                ++last_ind;
            }
        }
        return last_ind;
    }
    
};