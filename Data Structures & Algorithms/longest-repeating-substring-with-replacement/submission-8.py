class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_freq = 0
        left = 0
        res = 0

        for right in range(len(s)):
            freq_map[s[right]] = 1 + freq_map.get(s[right], 0)
            max_freq = max(freq_map.values())
            while (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                max_freq = max(max_freq, max(freq_map.values()))
                left += 1
            res = max(res, right - left + 1)
        return res


        # freq_map = {}
        # res = 0
        # left = 0
        # max_freq = 0

        # for right in range(len(s)):
        #     freq_map[s[right]] = 1 + freq_map.get(s[right], 0)
        #     max_freq = max(freq_map.values())
        #     while (right - left + 1) - max_freq > k:
        #         freq_map[s[left]] -= 1
        #         left += 1
            
        #     res = max(res, (right - left + 1))

        # return res