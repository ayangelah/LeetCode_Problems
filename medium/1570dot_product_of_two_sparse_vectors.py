# 1570 dot product of two sparse vectors

class SparseVector:
    def __init__(self, nums):
        self.nums_dict = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nums_dict[i] = nums[i]
    
    def dotProduct(self, vec):
        shared_indices = vec.nums_dict.keys().intersection(self.nums_dict.keys())

        total = 0
        while len(shared_indices) > 0:
            i = shared_indices.pop()
            total += vec.nums_dict[i] * self.nums_dict[i]
        
        return total