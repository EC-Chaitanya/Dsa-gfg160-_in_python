class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        r = [ -1]*n
        st = []
        for i in range(n):
            while st and arr[i] > arr[st[-1]]:
                index = st.pop()
                r[index] = arr[i]
            st.append(i)
        return r
