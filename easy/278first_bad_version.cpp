// The API isBadVersion is defined for you.
bool isBadVersion(int version);

#include <iostream>
using namespace std;

class Solution
{
public:
    int firstBadVersion(int n)
    {
        int floor = 0;
        int ceil = n;
        int curr;
        cout << floor << ceil << endl;
        while (ceil - floor > 1)
        {
            curr = (ceil - floor) / 2 + floor;
            if (isBadVersion(curr) == false)
            {
                floor = curr;
            }
            else
            {
                ceil = curr;
            }
        }
        if (ceil - floor == 1)
        {
            if (isBadVersion(ceil) == true)
                return ceil;
        }
        return floor;
    }
};