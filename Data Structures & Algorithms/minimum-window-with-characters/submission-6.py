class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tFreq: list[int] = [0] * 128
        for char in t:
            tFreq[ord(char)] += 1

        matchedChars: int = 0
        neededChars: int = sum(1 for t in tFreq if t != 0)

        window: list[int] = [0] * 128
        left: int = 0

        resLeft: int = -1
        resRight: int = len(s)

        for right in range(len(s)):
            window[ord(s[right])] += 1

            if (
                tFreq[ord(s[right])] != 0
                and window[ord(s[right])] == tFreq[ord(s[right])]
            ):
                matchedChars += 1

            while matchedChars == neededChars:
                if right - left < resRight - resLeft:
                    resLeft = left
                    resRight = right

                window[ord(s[left])] -= 1
                if (
                    tFreq[ord(s[left])] != 0
                    and window[ord(s[left])] < tFreq[ord(s[left])]
                ):
                    matchedChars -= 1

                left += 1

        return s[resLeft : resRight + 1] if resLeft != -1 else ""
