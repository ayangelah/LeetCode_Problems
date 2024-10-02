class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        regex_iter = 0
        str_iter = 0
        curr_preceding = None
        while True:
            print(regex_iter, str_iter)
            if str_iter > 0:
                curr_preceding = s[str_iter - 1]
            # process a character of the regex and a character of the string:
            # if p[regex_iter] == '*', set curr_preceding as s[str_iter].
            if p[regex_iter] == '*':
                # find how many repeating curr_preceding characters there might be in s
                i = 0
                while str_iter + i < len(s) and s[str_iter + i] == curr_preceding:
                    i += 1
                # find how many repeating curr_preceding characters there might be in s
                j = 0
                while regex_iter + j + 1 < len(p) and p[regex_iter + j + 1] == curr_preceding:
                    j += 1
                amount_absorbed_by_star = i - j
                print(amount_absorbed_by_star)
                if amount_absorbed_by_star < 0: # there are more curr_preceding in regex than in string
                    print("false1")
                    return False
                else:
                    str_iter += amount_absorbed_by_star
                    regex_iter += 1
                    print("here")
                    print(str_iter, regex_iter)

            # if p[regex_iter] == '.', both iters skip one character.
            elif p[regex_iter] == '.':
                regex_iter += 1
                str_iter += 1
            # else check if p[regex_iter] == s[str_iter]:
            else:
                if p[regex_iter] != s[str_iter]: # case #1 mismatch: there is a discrepency between the regex and string
                    if regex_iter + 1 < len(p) and p[regex_iter + 1] == '*':
                        regex_iter += 2 # the star can cancel out the existence of the conflicting str element
                    else:
                        print("false2")
                        return False
                else:
                    regex_iter += 1
                    str_iter += 1
                    print("there")
                    print(regex_iter, str_iter)
            
            # case match: both regex_iter and str_iter are at the end of the regex and string
            if regex_iter == len(p) - 1 and str_iter == len(s) - 1:
                special_characters = ['*', '.']
                if p[regex_iter] not in special_characters:
                    return p[regex_iter] == s[str_iter]
                return True

            # case #2 mismatch: there is still string left and we've run out of regex
            elif regex_iter > len(p) - 1:
                print("false3")
                return False

            # case #3 mismatch: there is still regex left and we've run out of string
            elif str_iter > len(s) - 1:
                print("false4")
                return False
