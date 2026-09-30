class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, one in enumerate(nums):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = one + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.add((one, nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return list(res)

        