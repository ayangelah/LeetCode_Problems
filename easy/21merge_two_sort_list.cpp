
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
    ListNode *mergeTwoLists(ListNode *list1, ListNode *list2)
    {
        // iterate through one list, when something is less than the one after, insert it
        ListNode *solution;
        ListNode *merger;
        if (list1 == nullptr)
            return list2;
        if (list2 == nullptr)
            return list1;
        if (list1->val < list2->val)
        {
            solution = list1;
            merger = list2;
        }
        else
        {
            solution = list2;
            merger = list1;
        }
        ListNode *curr = solution;
        while (merger != nullptr)
        {
            while (curr->next != nullptr && curr->next->val < merger->val)
            {
                curr = curr->next;
            }
            ListNode *temp = merger->next;
            merger->next = curr->next;
            curr->next = merger;
            merger = temp;
        }
        return solution;
        /* old solution
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;
        ListNode* holder = list1->next;
        while (curr1 != nullptr) {
            if (curr1->val <= curr2->val) {
                holder = curr1->next;
                curr1->next = curr2->next;
                curr2->next = curr1;
                curr1 = holder;
            }
            else {
                curr1 = curr1->next;
                curr2 = curr2->next;
            }
        }
        return curr2;
        */
    }
};