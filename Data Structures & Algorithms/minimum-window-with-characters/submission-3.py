class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        countT = Counter(t)
        window = {}
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            if window[c] == countT.get(c, 0):
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if window[s[left]] < countT.get(s[left],0):
                    have -= 1
                left += 1
        left, right = res
        return s[left : right + 1] if resLen != float("infinity") else ""