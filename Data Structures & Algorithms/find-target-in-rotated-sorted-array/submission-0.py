class Solution:
    def min_idx(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                return left
            
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        
        return right

    def search(self, nums: List[int], target: int) -> int:
        min_idx = self.min_idx(nums)

        left, right = 0, len(nums) - 1 # default to min_idx == 0

        if min_idx != 0:
            # target in right section
            if nums[min_idx] <= target <= nums[-1]:
                left = min_idx
            else:
                right = min_idx - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1

        