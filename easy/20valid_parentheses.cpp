#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
    bool isValid(string s)
    {
        vector<char> stack;
        for (int i = 0; i < s.size(); i++)
        {
            if (stack.size() > 0)
                cout << stack.back();
            switch (s[i])
            {
            case '(':
                stack.push_back('(');
                break;
            case '[':
                stack.push_back('[');
                break;
            case '{':
                stack.push_back('{');
                break;
            case ')':
                if (stack.size() != 0 && stack.back() == '(')
                {
                    stack.pop_back();
                }
                else
                    return false;
                break;
            case ']':
                if (stack.size() != 0 && stack.back() == '[')
                {
                    stack.pop_back();
                }
                else
                    return false;
                break;
            case '}':
                if (stack.size() != 0 && stack.back() == '{')
                {
                    stack.pop_back();
                }
                else
                    return false;
                break;
            }
        }
        if (stack.size() != 0)
            return false;
        return true;
    }
};