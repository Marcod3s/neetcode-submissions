"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        table = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            table[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = table[curr]
            copy.next = table[curr.next]
            copy.random = table[curr.random]
            curr = curr.next
        
        return table[head]