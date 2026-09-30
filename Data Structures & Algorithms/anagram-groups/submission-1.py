class Solution:
    def char_freq(self, word: str) -> Tuple[int]:
        res = [0] * 26

        for char in word:
            idx = ord(char) - ord("a")
            res[idx] += 1
        
        return tuple(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = self.char_freq(word)
            
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        return list(groups.values())
        