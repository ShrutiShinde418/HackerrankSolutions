# Problem: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            curr = self.root
            while True:
                if data <= curr.data:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new
                        break
                elif data > curr.data:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new
                        break
                else:
                    break


# time complexity: O(n)
# space complexity: O(n)
def levelOrder(root):
    queue = [root]
    result = []
    if root is None:
        return
    else:
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print(*result)


def levelOrderTraversal(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.insert(arr[i])
    levelOrder(tree.root)
    # levelOrderTraversal(tree.root)
