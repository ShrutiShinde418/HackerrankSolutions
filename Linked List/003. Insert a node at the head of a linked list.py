# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?isFullScreen=true


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_list(head):
    while head:
        print(head.data)
        head = head.next


# time complexity: O(1)
# space complexity: O(1)

def insertNodeAtHead(llist, data):
    new = SinglyLinkedListNode(data)
    if llist is None:
        llist = new
    else:
        new.next = llist
        llist = new
    return llist


if __name__ == "__main__":
    llist = SinglyLinkedList()
    for _ in range(int(input())):
        item = int(input())
        llist_head = insertNodeAtHead(llist.head, item)
        llist.head = llist_head
    print_list(llist.head)
