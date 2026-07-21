# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        curr = head
        sz = 0
        while curr:
            curr = curr.next
            sz += 1
        
        if n == sz:
            head = head.next
            return head

        sz = sz - n

        curr = head
        count = 1
        while count < sz:
            curr = curr.next
            count += 1
        curr.next = curr.next.next

        return head