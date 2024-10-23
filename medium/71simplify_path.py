class Solution:
    def simplifyPath(self, path: str) -> str:
        # deal with the cases for .., ., //, trailing /, iterate backwards
        # turn into array separated by /, then deal with . and ..
        path_array = []
        curr = None
        for i in range(len(path)):
            if path[i] == '/' and curr is not None:
                path_array.append(curr)
                curr = None
            elif path[i] != '/':
                if curr == None:
                    curr = path[i]
                else:
                    curr += path[i]
        if curr is not None:
            path_array.append(curr)
        
        # deal with . and ..
        j = 0
        while j < len(path_array):
            if path_array[j] == '.':
                path_array.pop(j)
            elif path_array[j] == '..':
                path_array.pop(j)
                if j > 0:
                    path_array.pop(j-1)
                    j -= 1
            else:
                j += 1
        
        # turn into string
        return '/' + '/'.join(path_array)