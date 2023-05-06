# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    jumps = 0
    distance = Y - X

    jumps += distance // D

    if(distance % D > 0):
        jumps += 1

    return jumps
