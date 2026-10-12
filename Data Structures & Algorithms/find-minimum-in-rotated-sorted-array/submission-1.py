class Solution:
    def findMin(self, nums: List[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                return nums[left]

            mid: int = (left + right) // 2

            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] >= nums[left]:
                left = mid + 1
        
        return nums[right]

        