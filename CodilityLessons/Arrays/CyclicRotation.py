# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if(len(A) == 0):
        return A
    
    currElement = None
    for i in range(K):
        currElement = A[0]
        for j in range(1,len(A)):
            

            temp = A[j]
            A[j] = currElement
            currElement = temp

            if(j == len(A) - 1):
                A[0] = currElement



    return A
