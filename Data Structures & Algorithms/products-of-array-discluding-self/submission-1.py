class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res: list[int] = [1 for num in nums]
        running = nums[0]
        for i in range(1, len(res)):
            res[i] *= running
            running *= nums[i]
        
        running = nums[-1]
        for i in range(len(res) - 2, -1, -1):
            res[i] *= running
            running *= nums[i]
        
        return res
        