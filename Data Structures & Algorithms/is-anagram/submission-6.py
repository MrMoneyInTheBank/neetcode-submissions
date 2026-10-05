class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def freq_array(s: str) -> list[int]:
            freq: list[int] = [0] * 26

            for char in s:
                idx = ord(char) - ord("a")
                freq[idx] += 1
        
            return freq
        
        return freq_array(s) == freq_array(t)

        