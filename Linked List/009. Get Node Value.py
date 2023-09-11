# Problem: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem?isFullScreen=true


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


def getNode(llist, positionFromTail):
    p = q = llist
    for i in range(positionFromTail):
        p = p.next
    while p.next:
        q = q.next
        p = p.next
    return q.data


# time complexity: O(n)
# space complexity: O(1)


def position_from_tail(llist, positionFromTail):
    p = q = llist
    k = 0
    while p.next:
        k += 1
        p = p.next
    if k == positionFromTail:
        return llist.data
    else:
        t = k - positionFromTail
        while t != 0:
            q = q.next
            t -= 1
        return q.data


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        llist = SinglyLinkedList()
        for i in range(n):
            item = int(input())
            llist.insert(item)
        position = int(input())
        result = getNode(llist.head, position)
        print(result)
