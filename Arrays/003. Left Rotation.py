# Problem: https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true

# iteratively

# time complexity: O(n^2)
# space complexity: O(1)
def rotateLeft_1(d, arr):
    for i in range(d):
        temp = arr[0]
        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]
        arr[-1] = temp
    return arr


# shortcut

# time complexity: O(n)
# space complexity: O(1)
def rotateLeft(d, arr):
    x = d % len(arr)
    return arr[x:] + arr[:x]


if __name__ == "__main__":
    n, d = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    result = rotateLeft(d, arr)
    print(*result)
