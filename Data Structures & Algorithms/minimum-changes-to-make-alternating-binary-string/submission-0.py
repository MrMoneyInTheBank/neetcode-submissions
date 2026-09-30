class Solution:
    def alternate(self, s: str, start: int) -> int:
        curr = start
        res = 0

        for i in range(len(s)):
            if s[i] != str(curr):
                res += 1
            curr ^= 1

        return res

    def minOperations(self, s: str) -> int:
        return min(self.alternate(s, 0), self.alternate(s, 1))

        