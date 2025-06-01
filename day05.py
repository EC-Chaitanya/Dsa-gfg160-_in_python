class Solution:
    # Function to find the elements appearing more than n/3 times
    def findMajority(self, arr):
        n = len(arr)
        # Step 1: Find up to two potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify the counts of the candidates
        result = []
        for candidate in [candidate1, candidate2]:
            if arr.count(candidate) > n // 3:
                result.append(candidate)

        return sorted(result)

# Test
arr = [2, 1, 5, 5, 5, 6, 6, 6]
obj = Solution()
print(obj.findMajority(arr))  # Output: [5, 6]


                
