class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        # Using dummy head and tail simplifies boundary edge cases
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        # Traverse from the closer end
        if index < self.size // 2:
            curr = self.left.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.right.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        # Find the node currently at index
        if index < self.size // 2:
            succ = self.left.next
            for _ in range(index):
                succ = succ.next
        else:
            succ = self.right
            for _ in range(self.size - index):
                succ = succ.prev

        pred = succ.prev
        new_node = ListNode(val, succ, pred)
        pred.next = new_node
        succ.prev = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Find the node to delete
        if index < self.size // 2:
            curr = self.left.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.right.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        pred, succ = curr.prev, curr.next
        pred.next = succ
        succ.prev = pred

        self.size -= 1