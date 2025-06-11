#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        if len(arr)< 2:
            return[]
        arr.sort()
        i ,j = 0 , len(arr)-1
        closetdiff = float('inf')
        bestpair= []
        maxAbsDiff = -1
        while i < j:
            a, b = arr[i], arr[j]
            s = a + b
            diff = abs(s - target)
            if diff< closetdiff or (diff== closetdiff and abs(a- b)>maxAbsDiff):
                bestpair = a, b
                closetdiff = diff
                maxAbsDiff =abs(a-b)
            if s < target:
                i += 1
                
            else:
                j -= 1
        return bestpair
