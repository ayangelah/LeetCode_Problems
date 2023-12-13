#include <string>
using namespace std;

class Solution
{
public:
    string removeStars(string s)
    {
        /* too slow, tried to do it in-place
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '*') {
                s[i] = '_';
                for (int j = i-1; j >= 0; j--) {
                    if (s[j] != '*' and s[j] != '_') {
                        s[j] = '_';
                        break;
                    }
                }
            }
        }
        // deleting all the blanks
        int k = 0;
        while (k < s.size()) {
            if (s[k] == '_') {
                s.erase(k, 1);
            }
            else {
                k++;
            }
        }
        return(s);*/
        string ans = "";
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] != '*')
            {
                ans += s[i];
            }
            else
            {
                ans.pop_back();
            }
        }
        return (ans);
    }
};