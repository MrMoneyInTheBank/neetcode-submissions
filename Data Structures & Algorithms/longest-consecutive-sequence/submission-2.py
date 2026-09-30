class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 in num_set:
                continue
            else:
                curr = 1
                idx = num
                while idx + 1 in num_set:
                    curr += 1
                    idx += 1
                res = max(res, curr)
        
        return res
                    