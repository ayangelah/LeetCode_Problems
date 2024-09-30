class Solution:
    def intToRoman(self, num: int) -> str:
        # start with leftmost digit/largest value of roman numeral that fits into num
        roman_dict = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        
        num_list = str(num)
        roman_equivalent = ""
        for i, digit in enumerate(num_list):
            length = len(num_list)
            digit = int(digit)
            
            # case 1: > 5 but not 9
            if digit > 5 and digit != 9:
                largest = 5 * 10**(length - i - 1)
                roman_equivalent += roman_dict[largest]
                ones = 10**(length - i - 1)
                for i in range(digit - 5):
                    roman_equivalent += roman_dict[ones]

            # case 2: its 9
            elif digit == 9:
                largest = 10**(length - i)
                subtractant = 10**(length - i - 1)
                roman_equivalent += (roman_dict[subtractant] + roman_dict[largest])

            # case 3: < 5 but not 4
            elif digit < 5 and digit != 4:
                largest = 10**(length - i - 1)
                for i in range(digit):
                    roman_equivalent += roman_dict[largest]

            # case 4: its 4
            elif digit == 4:
                largest = 5 * 10**(length - i - 1)
                subtractant = 10**(length - i - 1)
                roman_equivalent += (roman_dict[subtractant] + roman_dict[largest])

            # case 5: its 5
            else:
                largest = 5 * 10**(length - i - 1)
                roman_equivalent += roman_dict[largest]

        return roman_equivalent