class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx_reach = 0
        for i in range(len(nums)):
            if i > mx_reach:
                return False
            mx_reach = max(mx_reach,nums[i] + i)
            if mx_reach >= len(nums)-1:
                return True






