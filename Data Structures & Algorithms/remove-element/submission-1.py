class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        res: int = len(nums)

        while left <= right:
            if nums[left] != val:
                left += 1
            elif nums[right] == val:
                res -= 1
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                res -= 1
                left += 1
                right -= 1

        return res
        