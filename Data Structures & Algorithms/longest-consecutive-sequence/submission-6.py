class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        numSet: set[int] = set(nums)
        res: int = 1

        for num in nums:
            if num - 1 in numSet:
                continue
            else:
                curr = 1

                while num + 1 in numSet:
                    curr += 1
                    num += 1

                res = max(res, curr)

        return res

