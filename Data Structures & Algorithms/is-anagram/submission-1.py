from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = Counter(s)
        freq_t = Counter(t)

        for char, freq in freq_s.items():
            if char not in freq_t or freq_t[char] != freq:
                return False
                
        for char, freq in freq_t.items():
            if char not in freq_s or freq_s[char] != freq:
                return False
        return True
        