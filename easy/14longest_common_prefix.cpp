using namespace std;
#include <iostream>
#include <vector>

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        string solution;
        int shortestlength = strs[0].size();
        int counter = 0;
        char currchar;
        // determine shortest length:
        for (int i = 1; i < strs.size(); i++)
        {
            if (strs[i].size() < shortestlength)
                shortestlength = strs[i].size();
        }
        // iterate through how many letters
        for (int a = 0; a < shortestlength; a++)
        {
            // iterate through strs
            currchar = strs[0][counter];
            cout << currchar;
            for (int i = 1; i < strs.size(); i++)
            {
                if (counter >= strs[i].size())
                    return solution;
                if (currchar != strs[i][counter])
                    return solution;
            }
            solution += currchar;
            counter++;
        }
        return solution;
    }
};