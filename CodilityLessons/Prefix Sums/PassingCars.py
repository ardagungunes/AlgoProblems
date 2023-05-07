# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    zeros = 0
    result = 0

    for i in range(len(A)):
        if(A[i] == 0):
            zeros += 1

        else:
            result += zeros

    if(result > 1000000000):
        return -1

    return result