class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_copy = {None: None}

        # First pass: create copies of all nodes and store mapping
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: assign next and random pointers
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]