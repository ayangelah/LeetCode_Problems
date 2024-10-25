class Solution:
    def myPow(self, x: float, n: int) -> float:
        # multiply in an exponential fashion
        # x^5 -> x^2*x^2*x

        # edge case 
        if n == 0:
            return 1
        
        # negative:
        if n < 0:
            x = 1 / x
        
        odd_remainder = 1
        curr_multiplicator = x
        pos_n = abs(n)
        while pos_n > 0:
            print(n, curr_multiplicator, odd_remainder)
            # odd case
            if pos_n % 2 == 1:
                odd_remainder *= curr_multiplicator
            curr_multiplicator *= curr_multiplicator
            pos_n //= 2
    
        return odd_remainder