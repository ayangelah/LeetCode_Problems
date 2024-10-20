# 339 nested list weight sum

def nested_list_weight_sum(nested_list):
    # iterate through and remove one depth at a time, multiplying the numbers found by depth.
    depth = 1
    depth_sum = 0
    while nested_list != []:
        i = 0
        next_list = []
        while i < len(nested_list): # iterating through with one depth
            if type(nested_list[i]) == int:
                depth_sum += nested_list.pop(i) * depth # removes the int and adds to depth sum
            else:
                next_list += nested_list[i]
                i += 1
        depth += 1
        nested_list = next_list
    return depth_sum

def tests():
    assert(nested_list_weight_sum([[1]]) == 2)
    assert(nested_list_weight_sum([[1, 1, 3]]) == 10)
    assert(nested_list_weight_sum([[1, 3], [1, 1], [[2]]]) == 18)
    assert(nested_list_weight_sum([[[[[[[]]]]]]]) == 0)
    print("passed all tests")