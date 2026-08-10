class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
