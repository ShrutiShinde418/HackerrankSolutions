# Problem: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem


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


# time complexity: O(n)
# space complexity: O(1)
def removeDuplicates(llist):
    ptr = llist
    while ptr.next:
        if ptr.data != ptr.next.data:
            ptr = ptr.next
        else:
            ptr.next = ptr.next.next
    return llist


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        llist = SinglyLinkedList()
        for _ in range(n):
            item = int(input())
            llist.insert(item)
        llist_head = removeDuplicates(llist.head)
        print_list(llist_head)
