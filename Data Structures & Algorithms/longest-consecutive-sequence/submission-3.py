class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set: set[int] = set(nums)
        res: int = 0

        for num in nums:
            if num - 1 in num_set:
                continue
            else:
                curr: int = 1

                while num + 1 in num_set:
                    curr += 1
                    num += 1
                
                res = max(res, curr)
        
        return res
        