class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Step 1: Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Step 3: Merge two halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2