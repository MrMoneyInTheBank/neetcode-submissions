class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def bt(idx: int, total: int):
            if total == target:
                res.append(curr[:])
                return
            if total > target or idx == len(nums):
                return
            curr.append(nums[idx])
            bt(idx, total + nums[idx])
            curr.pop()
            bt(idx + 1, total)

        bt(0, 0)
        return res