# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(N, A):
    
    
    counters = [0] * N
    maxNum = 0
    b = 0
    

    for i in range(len(A)):
        if(A[i] <= len(counters)):
            counters[A[i] - 1] = (max(b,counters[A[i] - 1]) + 1)
            if(counters[A[i] - 1] > maxNum):
                maxNum = counters[A[i] - 1]
            

        else:
            b = maxNum


    for i in range(len(counters)):
        if(counters[i] < b):
            counters[i] = b

    return counters