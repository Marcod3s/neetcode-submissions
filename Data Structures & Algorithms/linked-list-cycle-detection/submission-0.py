# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        current = head


        list = []
        while current:
            list.append(current)
            if current.next in list:
                return True
            current = current.next
        return False