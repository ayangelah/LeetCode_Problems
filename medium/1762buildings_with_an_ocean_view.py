# 1762 buildings with an ocean view

# go from the right, and keep a running max. If an index is greater than the running max, it has an ocean view, and should also update the max.
def solution(heights):
    running_max = 0
    ocean_views = []
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > running_max:
            ocean_views.append(i)
            running_max = heights[i]
    return ocean_views[::-1]

def tests():
    assert solution([4,2,3,1]) == [0,2,3]
    assert solution([4,3,2,1]) == [0,1,2,3]
    assert solution([1,3,2,4]) == [3]
    assert solution([2,2,2,2]) == [3]
    print("passed all cases")

tests()
