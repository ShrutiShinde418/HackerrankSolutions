# Problem: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?isFullScreen=true


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None


def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # time complexity: O(n)
    # space complexity: O(n)
    def insert(self, val):
        new = Node(val)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                if val <= current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new
                        break
                else:
                    break

    def insert_1(self, val):
        new = Node(val)
        if not self.root:
            self.root = new
            return
        curr = self.root
        while curr:
            if val <= curr.info:
                if curr.left is None:
                    curr.left = new
                    return
                curr = curr.left
            elif val > curr.info:
                if curr.right is None:
                    curr.right = new
                    return
                curr = curr.right


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())
    head = None
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.insert(arr[i])
    preOrder(tree.root)
