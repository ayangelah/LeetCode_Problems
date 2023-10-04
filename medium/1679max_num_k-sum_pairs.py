class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        removals = 0
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for j in freq:
            if k-j in freq:
                amount = min(freq[k-j], freq[j])
                if amount != 0:
                    if j == k-j:  # if same numbers
                        print("here1")
                        removals += freq[j]/2
                        freq[j] = freq[j] % 2
                        continue
                    else:  # if different numbers
                        freq[j] -= amount
                        freq[k-j] -= amount
                        removals += amount
        return removals
