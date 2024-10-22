from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # approach: heapify the array, remove items off of heap till hit k
        # heapify the array
        queue = list(range(len(nums)-1, -1, -1))
        while queue: # iterate through all parents
            i = queue.pop(0)
            larger_child = None
            if (i+1)*2 < len(nums) and nums[(i+1)*2] > nums[i] and nums[(i + 1)*2-1] < nums[(i + 1)*2]: # if right child is bigger
                larger_child = (i + 1)*2
            elif (i+1)*2-1 < len(nums) and nums[(i + 1)*2-1] > nums[i]: # if left child is bigger
                larger_child = (i + 1)*2-1
            else:
                continue
            temp = nums[i]
            nums[i] = nums[larger_child]
            nums[larger_child] = temp
            queue.append(larger_child)

        # remove k times:
        count = 1
        while count < k:
            # replace parent with largest child until reach leaf
            curr_index = 0
            while (curr_index + 1) * 2 - 1 < len(nums):
                next_index = None
                # choose the larger child
                if (curr_index + 1) * 2 < len(nums) and nums[(curr_index + 1) * 2] > nums[(curr_index + 1) * 2 - 1]: 
                    next_index = (curr_index + 1)*2
                else:
                    next_index = (curr_index + 1) * 2 - 1
                # swap with curr index
                temp = nums[next_index]
                nums[curr_index] = nums[next_index]
                nums[next_index] = temp
                curr_index = next_index
            nums[curr_index] = -10**4 - 1 # minimum
            count += 1
        return nums[0]