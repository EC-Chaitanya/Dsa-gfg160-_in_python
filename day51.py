
class Solution:
    def countTriplets(self, arr, target):
        # code here
        n = len(arr)
        c = 0
        for i in range(n -2):
            left = i + 1
            right = n - 1
            while left < right :
                curr_sum = arr[i] + arr[left] + arr[right]
                
                if curr_sum == target:
                    if arr[left] == arr[right]:
                        num_e = right - left + 1
                        c += (num_e *(num_e - 1)) //2
                        break
                    else:
                        left_c = 1
                        right_c = 1
                        while left + 1 <right and arr[left] == arr[left+1]:
                            left_c += 1
                            left += 1
                        while right - 1 > left and arr[right] == arr[right -1]:
                            right_c += 1
                            right -= 1
                        c += left_c * right_c
                        left += 1
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else :
                    right -= 1
        return c
