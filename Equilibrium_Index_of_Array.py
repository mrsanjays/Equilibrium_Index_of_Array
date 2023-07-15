class Solution:
    @staticmethod
    def Equilibrium(array):
        n=len(array)
        lsum=0
        totsum=0
        for element in array: 
            totsum+=element
        for i in range(n):
            if lsum==totsum-lsum-array[i]:
                return i
            lsum+=array[i]
        return -1
"""
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

PS:
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.
"""
if __name__ == '__main__':
    ob=Solution()
    array=list(map(int,input().split()))
    print(ob.Equilibrium(array))

