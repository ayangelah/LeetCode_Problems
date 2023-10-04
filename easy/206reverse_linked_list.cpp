
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
    ListNode *reverseList(ListNode *head)
    {
        ListNode *reversed;
        ListNode *end;
        if (head == nullptr)
            return head;
        if (head->next == nullptr)
        {
            return head;
        }
        else
        {
            reversed = reverseList(head->next);
            end = reversed;
            while (end->next != nullptr)
            {
                end = end->next;
            }
            end->next = head;
            head->next = nullptr;
            return reversed;
        }
    }
};