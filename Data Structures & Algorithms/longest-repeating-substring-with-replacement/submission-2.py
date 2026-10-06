class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left: int = 0
        res: int = 0
        window: dict[str, int] = {}

        for right in range(len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
                
            res = max(res, right - left + 1)
        
        return res
        