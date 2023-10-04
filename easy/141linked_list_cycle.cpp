#include <iostream>

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        ListNode *ptr1 = head;
        ListNode *ptr2 = head;

        if (ptr1 == nullptr || ptr2 == nullptr)
        {
            return false;
        }

        while (ptr1->next != nullptr && ptr2->next != nullptr)
        {
            if (ptr1->next->next == nullptr)
            {
                return false;
            }
            ptr1 = ptr1->next->next;
            ptr2 = ptr2->next;
            if (ptr1 == ptr2)
            {
                return true;
            }
        }
        return false;
    }
};