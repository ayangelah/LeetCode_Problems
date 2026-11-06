class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        bin_nums = [bin(num) for num in data]
        print(f"{bin_nums}")

        # constants
        one_byte_mask = 0b10000000
        one_byte_val = 0
        two_byte_mask = 0b11100000
        two_byte_val = 0b11000000
        three_byte_mask = 0b11110000
        three_byte_val = 0b11100000
        four_byte_mask = 0b11111000
        four_byte_val = 0b11110000
        tail_byte_mask = 0b11000000
        tail_byte_val = 0b10000000
        
        if not data:
            return False

        curr_front = 0
        curr = curr_front

        while curr_front < len(data):
            if data[curr_front] & one_byte_mask == one_byte_val: # one byte utf-8
                curr_front += 1
                curr = curr_front
                print("1")
            else:
                if data[curr_front] & two_byte_mask == two_byte_val:
                    if curr_front + 1 >= len(data):
                        return False
                    for i in range(1):
                        curr += 1
                        if data[curr] & tail_byte_mask != tail_byte_val:
                            return False
                    print("2")

                elif data[curr_front] & three_byte_mask == three_byte_val:
                    if curr_front + 2 >= len(data):
                        return False
                    for i in range(2):
                        curr += 1
                        if data[curr] & tail_byte_mask != tail_byte_val:
                            print(bin(data[curr]))
                            return False
                    print("3")
                
                elif data[curr_front] & four_byte_mask == four_byte_val:
                    if curr_front + 3 >= len(data):
                        return False
                    for i in range(3):
                        curr += 1
                        if data[curr] & tail_byte_mask != tail_byte_val:
                            return False
                    print("4")
                else:
                    return False
                
                curr_front = curr + 1
                curr = curr_front
        return True
