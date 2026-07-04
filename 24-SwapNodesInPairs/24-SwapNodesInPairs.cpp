// Last updated: 7/4/2026, 7:03:32 PM
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *dummy = new ListNode(0), *prev = dummy;
        dummy->next = head;
        while(prev->next && prev->next->next) {
            ListNode *a = prev->next, *b = prev->next->next;
            prev->next = b, a->next = b->next, b->next = a, prev = a;
        }
        head = dummy->next, delete dummy, prev;
        return head;
    }
};