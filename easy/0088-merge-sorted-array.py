class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # work backwards, take the largest number of the two and put it in the back of nums1
        if len(nums1) == 0 or len(nums2) == 0:
            return nums1
        
        i = m - 1
        j = n - 1
        end = n + m - 1
        while end >= 0:
            print(i, j)
            if nums1[i] > nums2[j] and i >= 0:
                nums1[end] = nums1[i]
                i -= 1
                print(f"index {end} is set as {nums1[i]}")
            elif nums1[i] <= nums2[j] and j >= 0:
                nums1[end] = nums2[j]
                j -= 1
                print(f"index {end} is set as {nums2[j]}")
            elif i < 0 and j >= 0:
                nums1[end] = nums2[j]
                j -= 1
                print(f"index {end} is set as {nums2[j]}")
            elif j < 0 and i >= 0:
                nums1[end] = nums1[i]
                i -= 1
                print(f"index {end} is set as {nums1[i]}")
            
            end -= 1
