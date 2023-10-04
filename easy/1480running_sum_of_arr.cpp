#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> runningSum(vector<int> &nums)
    {
        vector<int> solution = nums;
        for (int i = 1; i < nums.size(); i++)
        {
            solution[i] = solution[i - 1] + solution[i];
        }
        return solution;
    }
};