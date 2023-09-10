# Problem: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem?isFullScreen=true
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


# time complexity: O(n)
# space complexity: O(1)


def reverse(head):
    p = r = head
    q = None
    while p:
        r = p.next
        p.next = q
        q = p
        p = r
    return q


if __name__ == "__main__":
    llist = SinglyLinkedList()
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(n):
            item = int(input())
            llist.insert(item)
    llist_head = reverse(llist.head)
    print_list(llist_head)
