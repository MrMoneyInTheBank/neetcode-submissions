class Solution:

    def encode(self, strs: List[str]) -> str:
        res: str = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        res: list[str] = []
        idx: int = 0

        while idx < len(s):
            length: int = 0
            jdx: int = idx

            while s[jdx] != "#":
                length = length * 10 + int(s[jdx])
                jdx += 1
            
            res.append(s[jdx + 1: jdx + 1 + length])
            jdx += 1 + length
            idx = jdx
        
        return res
