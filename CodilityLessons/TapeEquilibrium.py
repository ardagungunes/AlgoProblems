# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    #In this problem we store 2 arrays:
    #One of them is sum of elements in every position of the array left to right
    #The other is sum of elements in every position of the array right to left
    #abs(arr1[i] - arr2[i+1]) will give us the differences in every position

    arr1 = [0] * len(A)
    arr2 = [0] * len(A)
    minDifference = float("inf")

    total = 0
    for i in range(len(A)):
        total += A[i]
        arr1[i] = total

    total = 0
    for j in range(len(A) - 1,-1,-1):
        total += A[j]
        arr2[j] = total
    

    for x in range(len(A) - 1):
        if(abs(arr1[x] - arr2[x+1]) < minDifference):
            minDifference = abs(arr1[x] - arr2[x+1])
    return minDifference
