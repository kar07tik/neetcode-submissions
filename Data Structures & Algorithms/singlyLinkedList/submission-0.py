class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, i: int) -> int:
        curr = self.head
        index = 0

        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            index += 1

        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)

        if not self.head:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = newNode

    def remove(self, i: int) -> bool:
        if not self.head:
            return False

        if i == 0:
            self.head = self.head.next
            return True

        curr = self.head
        index = 0

        while curr and curr.next:
            if index + 1 == i:
                curr.next = curr.next.next
                return True
            curr = curr.next
            index += 1

        return False

    def getValues(self) -> list[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values