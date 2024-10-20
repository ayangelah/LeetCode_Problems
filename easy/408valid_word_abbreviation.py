def valid_abbrev(word, abbr):
    if len(abbr) > len(word):
        return False
    # iterate through word and abbreviation together, if hit number in abbr, skip
    i = 0
    j = 0
    curr_num = None
    while i < len(word) and j < len(abbr):
        if abbr[j].isnumeric():
            if curr_num == None and abbr[j] == '0': # case with leading 0s and 0s
                return False
            elif curr_num == None: # new number
                curr_num = int(abbr[j])
            else:
                curr_num = curr_num*10 + int(abbr[j]) # continue processing the number
            j += 1 # increment
        elif word[i] == abbr[j]: # matching case
            i += 1
            j += 1
        else: # case where substitution has occurred
            if curr_num is None: # no substitution with numbers, simply a mismatch
                return False
            # skip curr_num amount in word
            if curr_num + i < len(word):
                i += curr_num
            else:
                return False
    return True

def tests():
    print("test1")
    assert(valid_abbrev("substitution", "12"))
    assert(valid_abbrev("substitution", "s10n"))
    assert(valid_abbrev("substitution", "sub4n4"))
    assert(valid_abbrev("substitution", "substitution"))
    assert(not valid_abbrev("substitution", "s55n"))
    assert(not valid_abbrev("substitution", "s010n"))
    assert(not valid_abbrev("substitution", "substitutio0n"))
    print("all tests succeeded")