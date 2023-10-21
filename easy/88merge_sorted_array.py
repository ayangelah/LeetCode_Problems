class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        size = m+n
        while i < m+n:
            if i < m and j < n and nums1[i] > nums2[j]:
                # shifting
                for k in range(size-2, i-1, -1):
                    nums1[k+1] = nums1[k]
                print(nums1[i], '->', nums2[j])
                nums1[i] = nums2[j]
                m += 1
                j += 1
                print("1: ", nums1)
            elif j < n and i >= m:
                # shifting
                for p in range(size-2, i-1, -1):
                    nums1[p+1] = nums1[p]
                print(nums1[i], '->', nums2[j])
                nums1[i] = nums2[j]
                m += 1
                j += 1
                print("2: ", nums1)
            elif j > n and i >= m:
                print("3: ", nums1)
                break
            i += 1
        return nums1
