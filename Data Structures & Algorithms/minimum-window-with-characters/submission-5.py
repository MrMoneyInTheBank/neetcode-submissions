class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tFreq = [0] * 128
        for char in t:
            tFreq[ord(char)] += 1

        matchedChars = 0
        neededChars = sum(1 for f in tFreq if f != 0)
        window = [0] * 128
        left = 0
        resLeft, resRight = -1, len(s)

        for right in range(len(s)):
            idx = ord(s[right])
            window[idx] += 1

            if tFreq[idx] != 0 and window[idx] == tFreq[idx]:
                matchedChars += 1

            while matchedChars == neededChars:
                if right - left < resRight - resLeft:
                    resLeft = left
                    resRight = right

                jdx = ord(s[left])
                window[jdx] -= 1

                if tFreq[jdx] != 0 and window[jdx] < tFreq[jdx]:
                    matchedChars -= 1
                left += 1

        return s[resLeft: resRight + 1] if resLeft != -1 else ""