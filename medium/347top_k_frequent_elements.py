from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for i in range(len(nums)):
            if nums[i] not in frequency_dict:
                frequency_dict[nums[i]] = 1
            else:
                frequency_dict[nums[i]] += 1
        
        sorted_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        result = []
        for j in range(k):
            result.append(sorted_dict[j][0])
        return result