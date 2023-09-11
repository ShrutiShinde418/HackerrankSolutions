# Problem: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?isFullScreen=true


class SinglyLinkedListNode:
    def __init__(self, data):
        self.next = None
        self.data = None


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
# space complexity: O(n)
# where n is the no of elements in the longer linked list


def compare_lists(llist1, llist2):
    while (llist1 and llist2) and (llist1.data == llist2.data):
        llist1, llist2 = llist1.next, llist2.next
    if llist1 == llist2 == None:
        return 1
    return 0


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        llist1 = SinglyLinkedList()
        for i in range(n):
            item = int(input())
            llist1.insert(item)
        m = int(input())
        llist2 = SinglyLinkedList()
        for i in range(m):
            ele = int(input())
            llist2.insert(ele)
        result = compare_lists(llist1.head, llist2.head)
        print(result)
