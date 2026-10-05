class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def encode(s: str) -> tuple[int]:
            freq = [0] * 26

            for char in s:
                freq[ord(char) - ord("a")] += 1
            
            return tuple(freq)
        
        groups: dict[tuple[int], list[int]] = {}
    
        for word in strs:
            key = encode(word)

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        return list(groups.values())
        