# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):

    result = 0
    difference = (B//K)-(A//K)

    if(A % K == 0):
        result += 1

    result += difference

    return result