class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for idx, num in enumerate(nums):
            comp: int = target - num

            if comp in seen:
                return [seen[comp], idx]
            else:
                seen[num] = idx

        return []
