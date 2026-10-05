class Solution:

    def encode(self, strs: List[str]) -> str:
        res: str = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res: list[str] = []
        idx: int = 0

        while idx < len(s):
            length: int = 0
            jdx: int = idx

            while s[jdx] != "#":
                length = length * 10 + int(s[jdx])
                jdx += 1
            
            jdx += 1
            string = s[jdx: jdx + length]
            res.append(string)
            jdx += length
            idx = jdx
        
        return res
