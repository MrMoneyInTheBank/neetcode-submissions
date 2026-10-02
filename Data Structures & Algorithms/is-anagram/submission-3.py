class Solution:
    def freq(self, s: str) -> dict[str, int]:
        res = {}

        for char in s:
            res[char] = res.get(char, 0) + 1
        
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        return self.freq(s) == self.freq(t)
        