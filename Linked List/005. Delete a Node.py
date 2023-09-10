# Problem: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem?isFullScreen=true


class SinglyLinkedListNode:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new
        else:
            self.tail.next = new
        self.tail = new


def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# time complexity: O(n) if position != 0
# time complexity: O(1) if position == 0
# space complexity: O(1)


def deleteNode(llist, position):
    if position == 0:
        llist = llist.next
    else:
        q = p = llist
        pos = 0
        while pos != position:
            q = p
            p = p.next
            pos += 1
        q.next = p.next
        p.next = None
    return llist


if __name__ == "__main__":
    llist = SinglyLinkedList()
    for i in range(int(input())):
        item = int(input())
        llist.insert(item)
    position = int(input())
    llist_head = deleteNode(llist.head, position)
    print_list(llist_head)
