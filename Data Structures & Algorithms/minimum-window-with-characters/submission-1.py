from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_freq = Counter(t)
        window = {}

        matched_chars, total_chars = 0, len(t_freq)
        res = ""

        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in t_freq and window[s[right]] == t_freq[s[right]]:
                matched_chars += 1
            
            while matched_chars == total_chars:
                if res == "" or right - left + 1 < len(res):
                    res = s[left: right + 1]
                
                window[s[left]] -= 1
                if s[left] in t_freq and window[s[left]] < t_freq[s[left]]:
                    matched_chars -= 1
                left += 1
        
        return res
        