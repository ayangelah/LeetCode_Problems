// sept 6, 2022 solution

#include <iostream>
using namespace std;

class Solution
{
public:
    bool isSubsequence(string s, string t)
    {
        // iterate through t skipping characters until you get s
        int j = 0;
        for (int i = 0; i < t.size(); i++)
        {
            if (t[i] == s[j])
            {
                j++;
            }
        }
        cout << j;
        if (j == (s.size()))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};