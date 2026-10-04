class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        p_two = nums[0]
        p_one = max(p_two, nums[1])
    
        for i in range(2, len(nums)):
            curr = max(nums[i] + p_two, p_one)
            p_two = p_one
            p_one = curr
        
        return p_one
        