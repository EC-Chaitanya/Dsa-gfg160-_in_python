class Solution:
     def getMaxArea(self,arr):
        #code here
        n = len(arr)
        stack = []
        ma = 0
        index = 0
        while index < n:
            if not stack or arr[stack[-1]] <= arr[index]:
                stack.append(index)
                index += 1
            else:
                ts = stack.pop()
                height = arr[ts]
                width = index if not stack else index - stack[-1] -1
                ma = max(ma, height * width)
        while stack:
            ts = stack.pop()
            height = arr[ts]
            width = index if not stack else index - stack[-1] -1
            ma = max(ma, height * width)
        return ma
