from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            # Calculate GCD of current and next node
            g = gcd(curr.val, curr.next.val)

            # Create new node
            new_node = ListNode(g)

            # Insert new node between curr and curr.next
            new_node.next = curr.next
            curr.next = new_node

            # Move to the original next node
            curr = new_node.next

        return head