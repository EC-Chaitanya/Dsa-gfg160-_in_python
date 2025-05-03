#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        if not arr:
            return -1
        l , r = 0 , len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) //2
            
            if arr[mid]== key:
                return mid
        
            if arr[l]<= arr[mid]:
                if arr[l] <= key < arr[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                if arr[mid] < key <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends