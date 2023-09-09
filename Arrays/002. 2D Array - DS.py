# Problem: https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

# time complexity: O(n^2)
# space complexity: O(n)
def hourglassSum(arr):
    sums = []
    for i in range(0, 4):
        for j in range(0, 4):
            s = (
                arr[i][j]
                + arr[i][j + 1]
                + arr[i][j + 2]
                + arr[i + 1][j + 1]
                + arr[i + 2][j]
                + arr[i + 2][j + 1]
                + arr[i + 2][j + 2]
            )
            sums.append(s)
    return max(sums)


if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().strip().split())))
    result = hourglassSum(arr)
    print(result)
