/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *add = NULL;
    struct ListNode *prev = NULL;
    struct ListNode *new_node = NULL;
    int carry = 0;
    
    // Loop until l1 and l2 reaches NULL
    while (l1 != NULL || l2 != NULL) {
        // Initialize new_node
        new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        
        // If l1 reached NULL
        if (l1 == NULL) {
            prev -> next = new_node;
            
            // Update new_node
            new_node -> val = l2 -> val + carry;
            new_node -> next = NULL;
            
            l2 = l2 -> next;
        }
        // If l2 reached NULL
        else if (l2 == NULL) {
            prev -> next = new_node;
            
            // Update new_node
            new_node -> val = l1 -> val + carry;
            new_node -> next = NULL;
            
            l1 = l1 -> next;
        }
        // If both l1 and l2 have more digits
        else {
            if (prev == NULL) {
                add = new_node;
            }
            else {
                prev -> next = new_node;
            }
            
            // Update new_node
            new_node -> val = l1 -> val + l2 -> val + carry;
            new_node -> next = NULL;
            
            // Update nodes
            l1 = l1 -> next;
            l2 = l2 -> next;
        }
        
        // Update carry
        if (new_node -> val > 9) {
            // Quotient
            carry = new_node -> val / 10;
            // Remainder
            new_node -> val = new_node -> val % 10;
        }
        else {
            carry = 0;
        }
        
        prev = new_node;
    }
    
    // If carry is nonzero
    if (carry > 0) {
        // Initialize new_node
        new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        prev -> next = new_node;
        
        // Update new_node
        new_node -> val = carry;
        new_node -> next = NULL;
    }
    
    return add;
}
