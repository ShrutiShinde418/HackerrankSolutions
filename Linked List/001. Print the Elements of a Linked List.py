# Problem: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true


# time complexity: O(n)
# space complexity: O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = new


def print_list(head):
    while head:
        print(head.data)
        head = head.next


if __name__ == "__main__":
    n = int(input())
    llist = SinglyLinkedList()
    for i in range(n):
        item = int(input())
        llist.insert(item)
    print_list(llist.head)
