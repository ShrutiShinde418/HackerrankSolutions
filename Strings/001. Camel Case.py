# Problem: https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

# time complexity: O(n)
# space complexity: O(1)
def camelcase(s):
    k = 0
    for i in s:
        if i.isupper():
            k += 1
    return k + 1


if __name__ == "__main__":
    s = input()
    result = camelcase(s)
    print(result)
