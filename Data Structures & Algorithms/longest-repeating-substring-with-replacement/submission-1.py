class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        res = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            while (right - left + 1) - max(window.values()) > k:
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]

                left += 1
            
            res = max(res, right - left + 1)
    
        return res

        