#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> buildArray(vector<int> &nums)
    {
        vector<int> a;
        int size = nums.size();
        for (int i = 0; i < size; i++)
        {
            a.push_back(nums[nums[i]]);
        }
        return a;
    }
};