# Problem: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=true


class DoubleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new = DoubleLinkedListNode(data)
        if self.head is None:
            self.head = new
        else:
            self.tail.next = new
            new.prev = self.tail
        self.tail = new


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# time complexity: O(n)
# space complexity: O(1)
def sortedInsert(llist, data):
    new = DoubleLinkedListNode(data)
    if llist is None:
        return new
    elif data <= llist.data:
        new.next = llist
        llist.prev = new
        return new
    else:
        p = llist
        while data > p.data:
            if p.next is None:
                p.next = new
                new.prev = p
                return llist
            elif data <= p.next.data:
                new.next = p.next
                new.prev = p
                p.next.prev = new
                p.next = new
                return llist
            else:
                p = p.next
        return llist


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        llist = DoublyLinkedList()
        for j in range(n):
            item = int(input())
            llist.insert(item)
        data = int(input())
        llist1 = sortedInsert(llist.head, data)
        print_list(llist1)
