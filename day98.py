import heapq
class Solution:
    def getMedian(self, arr):
        l = []
        r = []
        m = []
        for num in arr:
            if not l or num <= -l[0]:
                heapq.heappush(l, -num)
            else:
                heapq.heappush(r,num)
            if len(l) > len(r)+ 1:
                heapq.heappush(r, -heapq.heappop(l))
            elif len(r)> len(l):
                heapq.heappush(l, -heapq.heappop(r))
            if len(l) == len(r):
                median = (-l[0] + r[0])/2.0
            else:
                median = -l[0]
            m.append(median)
        return m
