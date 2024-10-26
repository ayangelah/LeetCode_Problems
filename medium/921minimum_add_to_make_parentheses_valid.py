class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_adds = 0
        open_stack = 0
        unopened_closed_count = 0
        for i in range(len(s)):
            if s[i] == '(':
                open_stack += 1
            elif open_stack == 0:
                unopened_closed_count += 1
            else:
                open_stack -= 1
        return open_stack + unopened_closed_count