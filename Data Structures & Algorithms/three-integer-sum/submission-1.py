class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen: set[tuple[int, int, int]] = set()
        res: list[list[int]] = []

        for idx in range(len(nums) - 2):
            left: int = idx + 1
            right: int = len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]

                if total == 0:
                    if (nums[idx], nums[left], nums[right]) not in seen:
                        seen.add((nums[idx], nums[left], nums[right]))
                        res.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
        