def solution(A):
    N = len(A)
    A = list(set(A))
    
    total = int((N*(N+1))/2)

    if(total == sum(A)):
        return 1

    return 0