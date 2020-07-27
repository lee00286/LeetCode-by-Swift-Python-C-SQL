/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode *p = NULL;
    struct ListNode *q = NULL;
    struct ListNode *r = NULL;
    
    if (head == NULL || head -> next == NULL) {
        return head;
    }
    
    p = head;
    q = p -> next;
    r = q -> next;
    
    q -> next = p;
    p -> next = swapPairs(r);
    
    return q;
}
