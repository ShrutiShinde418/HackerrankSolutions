# Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true


def simpleArraySum(arr):
    return sum(arr)


if __name__ == "__main__":
    ar_count = int(input())
    ar = list(map(int, input().split()))
    result = simpleArraySum(ar)
    print(result)
