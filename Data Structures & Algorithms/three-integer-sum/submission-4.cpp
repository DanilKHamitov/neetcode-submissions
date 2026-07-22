class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        
        for (int i = 0; i < nums.size(); i++) {
            // Пропускаем дубликаты для i
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int target = -nums[i];
            int j = i + 1;  // ← Важно: i + 1
            int k = nums.size() - 1;
            
            while (j < k) {
                int sum = nums[j] + nums[k];
                
                if (sum > target) {
                    k--;
                } else if (sum < target) {
                    j++;
                } else {
                    // Нашли тройку
                    res.push_back({nums[i], nums[j], nums[k]});
                    
                    // Пропускаем дубликаты для j и k
                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;
                    
                    j++;
                    k--;
                }
            }
        }
        
        return res;  // ← Не забываем вернуть результат
    }
};
