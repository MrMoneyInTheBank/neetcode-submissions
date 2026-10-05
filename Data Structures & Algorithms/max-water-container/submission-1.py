class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res: int = 0
        left: int = 0
        right: int = len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width

            res = max(res, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return res
        