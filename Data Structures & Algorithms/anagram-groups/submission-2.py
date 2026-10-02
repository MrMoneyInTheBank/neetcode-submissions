class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(s: str) -> tuple[int]:
            res = [0] * 26

            for char in s:
                idx = ord(char) - ord("a")
                res[idx] += 1
            
            return tuple(res)
        
        groups = {}

        for word in strs:
            key = encode(word)

            groups[key] = groups.get(key, []) + [word]

        return list(groups.values())