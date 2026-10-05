class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: set[tuple[int, int, int]] = set()

        for idx in range(len(nums) - 2):
            left: int = idx + 1
            right: int = len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]

                if total == 0:
                    res.add((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return [list(trip) for trip in res]
        