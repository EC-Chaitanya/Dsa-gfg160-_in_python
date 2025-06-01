#  implement the next permutation 
class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        def pivot(arr):
            p = 0
            for i in range(n-1, 0 , -1):
                if arr[i -  1] > arr[i]:
                  p = i 
                  break  
            if p == 0:
                arr.sort()
                return 
            s = n - 1   #swap
            while arr[p - 1] >= arr[s]:
                s = -1    

            arr[s], arr[p-1] = arr[p - 1], arr[s] 

            arr[p:] = sorted(arr[p:]) 
            return arr 
        return pivot(arr)     


a = Solution()
arr = [2, 4, 1, 7, 5, 0]
print(a.nextPermutation(arr)) 
