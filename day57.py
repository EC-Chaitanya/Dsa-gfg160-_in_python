from collections import defaultdict
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        if k > n:
            return []
        freq = defaultdict(int)
        result = []
        for i in range(k):
            freq[arr[i]] += 1
        result.append(len(freq))
        for i in range(k, n):
            og = arr[i - k]
            freq[og] -=1
            if freq [og] == 0:
                del freq[og]
            ic = arr[i]
            freq[ic] += 1
            result.append(len(freq))
        return result
