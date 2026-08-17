class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map_s, freq_map_t = {}, {}

        for i in range(len(s)):
            freq_map_s[s[i]] = 1 + freq_map_s.get(s[i], 0)
            freq_map_t[t[i]] = 1 + freq_map_t.get(t[i], 0)

        return freq_map_t == freq_map_s