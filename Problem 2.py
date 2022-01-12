"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Time: O(n)
# Space: O(1)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        curr = head
        while curr != None:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        p = head
        q = head.next
        while p != None:
            if p.random != None:
                q.random = p.random.next
            p = p.next.next
            if q.next != None:
                q = q.next.next
        p = head
        q = head.next
        ans = q
        while p != None:
            p.next = q.next
            if p.next != None:
                q.next = p.next.next
            p = p.next
            q = q.next
        return ans
