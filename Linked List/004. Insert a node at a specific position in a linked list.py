# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?isFullScreen=true


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new


def print_list(head):
    while head:
        print(head.data)
        head = head.next

# time complexity: O(n) if pos != 0
# time complexity: O(1) if pos == 0
# space complexity: O(1)

def insertNodeAtPosition(llist, data, position):
    pos = 0
    new = Node(data)
    if position == 0:
        new.next = llist
        llist = new
    else:
        q = p = llist
        while pos != position:
            q = p
            p = p.next
            pos += 1
        q.next = new
        new.next = p
    return llist


if __name__ == "__main__":
    linkedList = SinglyLinkedList()
    for i in range(int(input())):
        item = int(input())
        linkedList.insert(item)
    data = int(input())
    position = int(input())
    llist_head = insertNodeAtPosition(linkedList.head, data, position)
    print_list(llist_head)
