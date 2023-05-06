# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    dct = {}
    unpaired = None

    for num in A:
        dct[num] = dct.get(num,0) + 1
    
    for (key,value) in dct.items():
        if(value % 2 != 0):
            unpaired = key
            break

    return unpaired
