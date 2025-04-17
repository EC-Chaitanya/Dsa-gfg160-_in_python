class Solution:
    def maximumProfit(self, prices):
        # code here
         if not prices:
             return 0
         minPrice= float('inf')
         maxProfit = 0
         for p in prices:
             minPrice = min(p, minPrice)
             profit = p - minPrice
             maxProfit = max(profit, maxProfit)
         return maxProfit

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends