class Solution:
    def encode(self, strs: list[str]) -> str:
        res: str = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> list[str]:
        res: list[str] = []
        idx: int = 0

        while idx < len(s):
            jdx: int = idx
            length: int = 0

            while s[jdx] != "#":
                length = length * 10 + int(s[jdx])
                jdx += 1

            res.append(s[jdx + 1 : jdx + 1 + length])
            idx = jdx + 1 + length

        return res
