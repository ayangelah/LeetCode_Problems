from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # greedy solution: 
        nums_dict = {0: [-1]}
        running_sum = 0
        running_sums_array = []
        # make running sums dict
        for i in range(len(nums)):
            running_sum += nums[i]
            running_sums_array.append(running_sum)
            if running_sum not in nums_dict:
                nums_dict[running_sum] = [i]
            else:
                nums_dict[running_sum].append(i)
        
        # count the number of subarrays with j as a right index
        num_subarrays = 0
        for j in range(len(running_sums_array)):
            if running_sums_array[j] - k in nums_dict:
                for l in nums_dict[running_sums_array[j] - k]:
                    if l < j:
                        num_subarrays += 1
        
        return num_subarrays
            