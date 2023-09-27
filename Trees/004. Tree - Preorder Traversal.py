# Problem: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=true


class Node:
    def __init__(self, info):
        self.right = None
        self.left = None
        self.info = info


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        curr = self.root
        if self.root is None:
            self.root = new
        else:
            while True:
                if data <= curr.info:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new
                        break
                elif data > curr.info:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new
                        break
                else:
                    break


def preOrder(root):
    stack = list()
    if root is None:
        return
    stack.append(root)
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.info, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    print()


def preorder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preorder(root.left)
    preorder(root.right)


if __name__ == "__main__":
    t = int(input())
    arr = list(map(int, input().split()))
    tree = BinarySearchTree()
    for i in range(t):
        tree.insert(arr[i])
    preOrder(tree.root)
    # preorder(tree.root)
