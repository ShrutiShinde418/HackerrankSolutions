# Problem: https://www.hackerrank.com/challenges/tutorial-intro/problem?isFullScreen=true

# time complexity: O(n)
# space complexity: O(1)
def introTutorial(v, arr):
    for i in range(len(arr)):
        if arr[i] == v:
            return i
    # or use return arr.index(v)


if __name__ == "__main__":
    v = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().split()))
    result = introTutorial(v, arr)
    print(result)
