# Problem: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem?isFullScreen=true


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


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
# space complexity: O(n)
def mergeLists(head1, head2):
    ptr = temp = SinglyLinkedListNode(0)
    if not head1:
        return head2
    if not head2:
        return head1
    while head1 and head2:
        if head1.data < head2.data:
            ptr.next = head1
            head1 = head1.next
        else:
            ptr.next = head2
            head2 = head2.next
        ptr = ptr.next

    if head1:
        ptr.next = head1
    if head2:
        ptr.next = head2
    return temp.next


if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        llist1 = SinglyLinkedList()
        for j in range(n):
            item_1 = int(input())
            llist1.insert(item_1)
        m = int(input())
        llist2 = SinglyLinkedList()
        for k in range(m):
            item_2 = int(input())
            llist2.insert(item_2)
        llist_head = mergeLists(llist1.head, llist2.head)
        print_list(llist_head)
