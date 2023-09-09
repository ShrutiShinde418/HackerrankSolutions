# Problem: https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true


def reverseArray(a):
    return a[::-1]


# iterative way

# time complexity: O(n)
# space complexity: O(n)


def reverse(a):
    ar = list()
    for i in range(len(a) - 1, -1, -1):
        ar.append(a[i])
    return ar


# reversing using swapping

# time complexity: O(n)
# space complexity: O(1)


def reverse_swapping(a):
    start = 0
    end = len(a) - 1
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a


# recursively

# time complexity: O(n)
# space complexity: O(n)
def reverse_recursive(a, start, end):
    if start >= end:
        return
    a[start], a[end] = a[end], a[start]
    reverse_recursive(a, start + 1, end - 1)
    return a


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    result = reverseArray(arr)
    print(*result)
