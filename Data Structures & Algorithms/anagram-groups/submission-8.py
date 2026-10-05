class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def encode(s: str) -> tuple[int, ...]:
            freq: list[int] = [0] * 26

            for char in s:
                freq[ord(char) - ord("a")] += 1

            return tuple(freq)

        groups: dict[tuple[int, ...], list[str]] = {}

        for s in strs:
            key = encode(s)

            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)

        return list(groups.values())
