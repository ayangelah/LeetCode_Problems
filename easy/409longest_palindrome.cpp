#include <map>
#include <iostream>
using namespace std;

class Solution
{
public:
    int longestPalindrome(string s)
    {
        int count = 0;
        std::map<char, int> my_map;
        int i;
        for (i = 0; i < s.size(); i++)
        {
            my_map[s[i]]++;
        }
        for (auto i : my_map)
        {
            cout << i.first << " " << i.second << endl;
            count += i.second / 2;
        }
        if (s.size() > count * 2)
            return count * 2 + 1;
        return count * 2;
    }
};