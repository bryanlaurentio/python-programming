#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    a = list(a)
    b = list(b)
    score_a = 0
    score_b = 0
    for i in range(len(list(a))):
        if a[i] < b[i]:
            score_b += 1
        elif a[i] > b[i]:
            score_a += 1
    print(score_a, score_b)


if __name__ == '__main__':
    a = map(int, input().rstrip().split())

    b = map(int, input().rstrip().split())

    result = compareTriplets(a, b)