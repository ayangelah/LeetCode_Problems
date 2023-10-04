class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        left = 0
        right = len(height) - 1
        curr = 0
        while left != right:
            if height[left] < height[right]:
                curr = (right - left)*(height[left])
                left += 1
            else:
                curr = (right - left)*(height[right])
                right -= 1
            if curr > max:
                max = curr
        return max
