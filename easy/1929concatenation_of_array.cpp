#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> getConcatenation(vector<int> &nums)
    {
        vector<int> a = nums;
        for (int i = 0; i < nums.size(); i++)
        {
            a.push_back(a[i]);
        }
        return a;
    }
};