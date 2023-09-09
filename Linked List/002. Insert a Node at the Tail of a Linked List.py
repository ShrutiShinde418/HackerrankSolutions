# Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?isFullScreen=true

# time complexity: O(n)
# space complexity: O(1)
class SinglyLinkedListNode:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_list(head):
    p = head
    while p:
        print(p.data)
        p = p.next


def insertNodeAtTail(head, data):
    new = SinglyLinkedListNode(data)
    if head is None:
        head = new
    else:
        p = head
        while p.next:
            p = p.next
        p.next = new
    return head


if __name__ == "__main__":
    llist = SinglyLinkedList()
    for i in range(int(input())):
        item = int(input())
        llist_head = insertNodeAtTail(llist.head, item)
        llist.head = llist_head
    print_list(llist.head)
