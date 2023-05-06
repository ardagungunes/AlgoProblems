# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    countArr = [0] * (max(A) + 1)
    flag = False

    for i in range(len(A)):
        if(A[i] > 0):
            countArr[A[i]] += 1
            flag = True

    if(not flag):
        return 1

    for j in range(len(countArr)):
        if(j != 0):
            if(countArr[j] == 0):
                return j
    
    return j + 1