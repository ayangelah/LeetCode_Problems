class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # approach: add open parentheses indexes to a queue.
        # if a close parentheses is found, pop from stack. if stack is empty, remove this parenthesis
        # once finished parsing the whole string, return count + open_count
        count = 0
        stack = []
        remove_closing = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 0: # remove parenthesis
                    remove_closing.append(i)
                else:
                    stack.pop() # remove an opening parentheses
        new_string = ""
        j = 0
        while j < len(s):
            if j not in stack and j not in remove_closing:
                new_string += s[j]
            j += 1
        return new_string
        