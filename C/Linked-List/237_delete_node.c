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
    
    // Copy val in node -> next to node
    node -> val = node -> next -> val;
    
    // Set up pre and tr 
    pre = node;
    tr = node -> next;
    
    // Update pre
    pre -> next = tr -> next;
    
    // Delete node
    free(tr);
}
