class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in window:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            window[s[right]] = window.get(s[right], 0) + 1
            res = max(res, right - left + 1)
    
        return res
        