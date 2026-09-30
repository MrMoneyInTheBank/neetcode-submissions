class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for word in strs:
            token = str(len(word)) + "#" + word
            res.append(token)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        idx = 0

        while idx < len(s):
            length = 0

            while s[idx] != "#":
                length = length * 10 + int(s[idx])
                idx += 1
            
            idx += 1
            res.append(s[idx: idx + length])
            idx += length
        
        return res


