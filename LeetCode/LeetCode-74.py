class Solution:
    
    def binarySearch(self,arr,l,r,target):
        while(l <= r):
            mid = (l + int((r-l)/2))

            if(arr[mid] == target):
                return mid

            elif(arr[mid] < target):
                l = mid + 1

            elif(arr[mid] > target):
                r = mid - 1

        return l



    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        #We can loop through the matrices and perform binary search
        #for every elements but that way the time complexity will be
        #m*O(log(n))

        #Instead of the above approach we can store the last elements of every matrix
        #in a new array and perform a binary search. That way we can find the matrix we are
        #looking for. After that process we perform binary search one last time.

        lastElements = []

        for matrices in matrix:
            lastElements.append(matrices[n - 1])

        index1 = self.binarySearch(lastElements,0,m-1,target)


        if(index1 >= m):
            return False
            
        index2 = self.binarySearch(matrix[index1],0,n-1,target)

        if(matrix[index1][index2] == target):
            return True

        return False


