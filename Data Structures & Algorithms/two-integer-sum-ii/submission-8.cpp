class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ans(2);
        int left = 0;
        int right = numbers.size()-1;
        while (numbers[left] + numbers[right] != target) {
            if(numbers[left]+ numbers[right] > target) {
                --right;
            }
            else {
                ++left;
            }
        }
        ans[0] = left+1;
        ans[1] = right+1;
        return ans;
    }
};
