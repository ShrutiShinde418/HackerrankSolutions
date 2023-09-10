# Problem: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem?isFullScreen
# =true


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
        print(head.data)
        head = head.next


# time complexity: O(n)
# space complexity: O(1)
def reversePrint(llist):
    p = llist
    if p:
        reversePrint(p.next)
        print(p.data)


# time complexity: O(n)
# space complexity: O(n)
def reverse_print(llist):
    arr = []
    p = llist
    while p:
        arr.append(p.data)
        p = p.next
    for i in reversed(arr):
        print(i)


if __name__ == "__main__":

    t = int(input())
    for i in range(t):
        n = int(input())
        llist = SinglyLinkedList()
        for j in range(n):
            item = int(input())
            llist.insert(item)
        reverse_print(llist.head)
