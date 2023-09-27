# Problem: https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?isFullScreen=true


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
                if data > curr.info:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new
                        break
                elif data <= curr.info:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new
                        break
                else:
                    break


# time complexity: O(n)
# space complexity: O(n)
def inorder_iterative(root):
    current = root
    stack = list()
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.info, end=" ")
            current = current.right
        else:
            break
    print()


def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.info, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    t = int(input())
    arr = list(map(int, input().split()))
    tree = BinarySearchTree()
    for i in arr:
        tree.insert(i)
    inorder_iterative(tree.root)
    # inorder(tree.root)
