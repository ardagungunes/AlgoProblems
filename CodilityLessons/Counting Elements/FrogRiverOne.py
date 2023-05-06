# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    dct = {}
    counter = 0

    total = int((X*(X+1))/2)

    for i in range(len(A)):

        if(dct.get(A[i]) is None):
            counter += A[i]
            dct[A[i]] = A[i]
        
        if(counter == total):
            return i

        
    return -1