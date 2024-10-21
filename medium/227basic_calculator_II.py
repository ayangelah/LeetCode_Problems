class Solution:
    def calculate(self, s: str) -> int:
        # pandas order: first / * then + - in the order that they come in. Will do two passes over the expression and simplify.
        # change to array for mutability
        temp = []
        # remove spaces
        curr = 0
        for i in s:
            if i == ' ':
                continue
            elif i.isnumeric():
                curr = curr * 10 + int(i)
            else:
                temp.append(curr)
                curr = 0
                temp.append(i)
        temp.append(curr)
        
        # multiply/divide
        i = 0
        while i < len(temp):
            if temp[i] == '/':
                temp[i-1] = temp[i-1] // temp[i+1]
                temp.pop(i)
                temp.pop(i) # each mathematical function is thought of a set of three, two numbers and an operator. we are replacing these with the result of the operation.
            elif temp[i] == '*':
                temp[i-1] = temp[i-1] * temp[i+1]
                temp.pop(i)
                temp.pop(i) # replace with result of multiplication or division
            else:
                i += 1
        
        # add/subtract
        total = temp[0]
        for i in range(len(temp)):
            if temp[i] == '-':
                total -= temp[i+1]
            elif temp[i] == '+':
                total += temp[i+1]
        return total