class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        running = nums[0]

        for i in range(1, len(pref)):
            pref[i] = running
            running *= nums[i]
        
        running = nums[-1]
        for i in range(len(pref) - 2, -1, -1):
            pref[i] *= running
            running *= nums[i]
            
        return pref