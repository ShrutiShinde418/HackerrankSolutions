# Problem: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?isFullScreen=true
class DoublyLinkedListNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# time complexity: O(n)
# space complexity: O(1)


def reverse(llist):
    p = r = llist
    q = None
    while p:
        r = p.next
        p.next = q
        p.prev = r
        q = p
        p = r
    return q


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        llist = DoublyLinkedList()
        for i in range(n):
            item = int(input())
            llist.insert(item)
        result = reverse(llist.head)
        print_list(result)
