class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid

        if min(nums[l], nums[r]) == nums[l]:
            ind = l
        else:
            ind = r

        if nums[ind] == target:
            return ind

        
        if target > nums[len(nums) - 1]:
            left = 0
            right = ind - 1
        else:
            left = ind
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

            


                     
            
    

        