class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # result = []
        # freq_map = {}
        # frequency_array = [[] for i in range(len(nums) + 1)]

        # for num in nums:
        #     freq_map[num] = 1 + freq_map.get(num, 0)

        # for num, freq in freq_map.items():
        #     frequency_array[freq].append(num)

        # for idx in range(k-1, 0, -1):
        #     if frequency_array[idx]:
        #         for num in frequency_array[idx]:
        #             result.append(num)
            
        #         if len(result) == k:
        #             return result

        freq_array = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        for value, freq in count.items():
            freq_array[freq].append(value)


        for i in range(len(freq_array)-1, 0 , -1):
            if freq_array[i]:
                for num in freq_array[i]:
                    res.append(num)
                if len(res) == k:
                    return res
