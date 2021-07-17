# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # If at least one linked list is empty
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        # Save curr and head
        curr = ListNode(0)
        head = curr

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                # l1.val >= l2.val
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # If there's leftover
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2

        return head.next
