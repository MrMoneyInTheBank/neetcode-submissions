class Solution:
    def get_window_max(self, window: dict[str, int]) -> str:
        res = None
        freq = 0

        for char, f in window.items():
            if f > freq:
                freq = f
                res = char
        
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        res = 0
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            max_element = self.get_window_max(window)
            while (right - left + 1) - window[max_element] > k:
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]

                if left_char == max_element:
                    max_element = self.get_window_max(window)
                left += 1
            
            res = max(res, right - left + 1)
    
        return res

        