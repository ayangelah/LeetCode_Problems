class Solution:
    def maximumSwap(self, num: int) -> int:
        # basically you want a sorted str decreasing.
        # case 1: swap the largest number with the beginning. If the largest number is already at the beginning, do this for the rest of the string not including the beginning
        str_num = list(str(num))
        str_list = ''.join(recursive_helper(str_num))
        return int(str_list)
                
def recursive_helper(num_str):
    if len(num_str) < 2:
        return num_str

    max_index = 0
    for i in range(len(num_str)):
        if max_index != 0 and num_str[i] >= num_str[max_index]:
            max_index = i
        elif num_str[i] > num_str[max_index]:
            max_index = i
    
    if max_index != 0:
        temp = num_str[0]
        num_str[0] = num_str[max_index]
        num_str[max_index] = temp
        return num_str
    else:
        result = num_str[0:1] + recursive_helper(num_str[1:])
        return result
