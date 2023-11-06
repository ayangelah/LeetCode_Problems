class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # check if DAG = checking if there are cycles
        # populating the dictionary
        # creates empty array of empty arrays
        d = [[] for i in range(numCourses)]
        for prerequisite in prerequisites:
            d[prerequisite[0]].append(prerequisite[1])
        print(d)

        # build the topological sort
        tobeprocessed = set()
        for i in range(len(d)):
            if d[i] == []:
                tobeprocessed.add(i)

        while tobeprocessed:
            print(tobeprocessed)
            temp = set()
            for k in range(len(d)):
                tempcourses = list(d[k])
                for course in tempcourses:
                    if course in tobeprocessed:
                        d[k].remove(course)
                        if d[k] == []:
                            temp.add(k)
            tobeprocessed = temp

        # if not possible, return false, otherwise, true.
        for j in range(len(d)):
            if d[j] != []:
                print(d)
                return False
        return True
