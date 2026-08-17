class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # freq_map_s, freq_map_t = {}, {}
        # if len(s) != len(t):
        #     return False
        
        # for id in range(len(s)):
        #     freq_map_s[s[id]] = 1 + freq_map_s.get(s[id], 0)
        #     freq_map_t[t[id]] = 1 + freq_map_t.get(t[id], 0)

        # if freq_map_s == freq_map_t:
        #     return True
        # return False

        if len(s) != len(t):
            return False

        freq_map_s, freq_map_t = {}, {}

        for i in range(len(s)):
            freq_map_s[s[i]] = 1 + freq_map_s.get(s[i], 0)
            freq_map_t[t[i]] = 1 + freq_map_t.get(t[i], 0)

        return freq_map_t == freq_map_s