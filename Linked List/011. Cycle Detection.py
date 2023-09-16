# Problem: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


# time complexity: O(n)
# space complexity: O(1)
def has_cycle(head):
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    return 0


if __name__ == "__main__":
    for i in range(int(input())):
        # cycle starts at this index
        index = int(input())
        n = int(input())
        llist = SinglyLinkedList()
        for i in range(n):
            item = int(input())
            llist.insert(item)
        extra = Node(-1)
        temp = llist.head

        for i in range(n):
            if i == index:
                extra = temp

            if i != n - 1:
                temp = temp.next

        temp.next = extra
        result = has_cycle(llist.head)
        print(result)
