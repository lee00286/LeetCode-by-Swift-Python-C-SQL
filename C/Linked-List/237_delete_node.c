/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    
    // Predecessor Pointer
    struct ListNode *pre = NULL;
    // Traversal Pointer
    struct ListNode *tr = NULL;
    
    pre = node;
    tr = node -> next;
    
    // Copy the 
    node -> val = tr -> val;
    
    // Predecessor Pointer
    struct ListNode *pre = NULL;
    // Traversal Pointer
    struct ListNode *tr = NULL;
    
    // Set up pre and tr
    pre = head;
    tr = head -> next;
    
    // If node == head
    if (pre -> val == node -> val) {
        free(pre);
        head = tr;
    }
    
    // If node != head and node != tail
    while (tr != NULL) {
        // Found the node we want to delete
        if (node -> val == tr -> val) {
            // Update pre
            pre -> next = tr -> next;
            // Delete node
            free(tr);
            break;
        }
    }
    
    // Head didn't change
}
