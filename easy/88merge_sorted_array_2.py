from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        last = n+m - 1
        while i >= 0 or j >= 0:
            # iterate from the end to avoid shifting
            if i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[last] = nums1[i]
                    i -= 1
                else:
                    nums1[last] = nums2[j]
                    j -= 1
                last -= 1
            else:
                if j >= 0:
                    nums1[:last+1] = nums2[:j+1]
                    j = -1
                else:
                    break
        return
        