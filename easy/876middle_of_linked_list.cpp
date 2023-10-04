#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {
        ListNode *counter = head;
        int count = 0;
        while (counter != nullptr)
        {
            count++;
            counter = counter->next;
        }
        int skipcount = count / 2;
        cout << skipcount;
        counter = head;
        while (skipcount > 0)
        {
            counter = counter->next;
            skipcount--;
        }
        return counter;
    }
};