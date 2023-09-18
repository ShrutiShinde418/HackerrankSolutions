# Problem: https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true

# time complexity: O(nlogn)
# space complexity: O(1)
def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))


if __name__ == "__main__":
    n = int(input())
    unsorted = []
    for i in range(n):
        item = input()
        unsorted.append(item)
    result = bigSorting(unsorted)
    print("\n".join(result))
