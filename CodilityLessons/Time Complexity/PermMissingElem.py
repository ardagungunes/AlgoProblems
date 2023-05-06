# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A) + 1

    total = int((N*(N+1))/2)

    return total - sum(A)
