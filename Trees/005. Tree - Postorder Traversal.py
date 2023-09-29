# Problem: https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?isFullScreen=true


class Node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            current = self.root
            while True:
                if data <= current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = new
                        break
                elif data > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = new
                        break
                else:
                    break


# time complexity: O(n)
# space complexity: O(n)
def postOrder(root):
    if root is None:
        return
    s1 = list()
    s2 = list()
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        node = s2.pop()
        print(node.info, end=" ")
    print()


def postOrder_recursive(root):
    if root is None:
        return
    postOrder_recursive(root.left)
    postOrder_recursive(root.right)
    print(root.info, end=" ")


if __name__ == "__main__":
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.insert(arr[i])
    postOrder(tree.root)
    postOrder_recursive(tree.root)
