#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zero += 1
    result_positive = float(positive/len_arr)
    result_negative = float(negative/len_arr)
    result_zero = float(zero/len_arr)

    print(result_positive)
    print(result_negative)
    print(result_zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
