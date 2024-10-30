from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # put all numbers and the number of their occurences in a dict
        # build triplets
        nums_dict = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in nums_dict:
                nums_dict[sorted_nums[i]] = [i]
            else:
                nums_dict[sorted_nums[i]].append(i)
        
        # sort dict keys to build unique triplets
        set_of_triplets = set()
        for j in range(len(sorted_nums)):
            for k in range(j+1, len(sorted_nums)):
                third_item = - (sorted_nums[j] + sorted_nums[k])
                if third_item in nums_dict and nums_dict[third_item][-1] > k:
                    set_of_triplets.add((sorted_nums[j], sorted_nums[k], third_item))
            
        return list(set_of_triplets)