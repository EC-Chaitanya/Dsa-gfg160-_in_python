from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        return heapq.nsmallest(k, points , key = lambda point: point[0]**2 +  point[1]**2)
        
        
