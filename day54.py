#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        l = 0
        r = len(arr)-1
        c = 0
        while l < r:
            curr_sum = arr[l] + arr[r]
            if curr_sum == target:
               if arr[l] == arr[r]:
                   n = r - l + 1
                   c += n*(n-1) //2
                   break
               else:
                   l_c = 1
                   r_c = 1
                   while l + 1 < r and arr[l] == arr[l + 1]:
                        l_c += 1
                        l += 1 
                   while r - 1 > l and arr[r] == arr[r-1]:
                        r_c += 1
                        r -= 1
                   c += l_c * r_c
                   l += 1
                   r -= 1
            elif curr_sum < target:
                l += 1
            else:
                r -= 1
                    
                
        return c
