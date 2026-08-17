class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_chart = [[] for i in range(len(nums) + 1)]
        res = []
        freq_map = {}
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        for num, freq in freq_map.items():
            print(freq)
            freq_chart[freq].append(num)

        for i in range(len(freq_chart) - 1, -1, -1):
            if freq_chart[i]:
                for num in freq_chart[i]:
                    res.append(num)

                if len(res) == k:
                    return res

        return res





















        # res = []
        # frequency_array = [[] for i in range(len(nums) + 1)]
        # freq_map = {}

        # for num in nums:
        #     freq_map[num] = 1 + freq_map.get(num, 0)


        # for num, freq in freq_map.items():
        #     frequency_array[freq].append(num)

        # for idx in range(len(frequency_array) - 1, 0, -1):
        #     if frequency_array[idx]:
        #         for num in frequency_array[idx]:
        #             res.append(num)
        #         if len(res) == k:
        #             return res






