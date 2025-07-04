import heapq

def k_largest_elements(arr, k):
    # Get k largest elements using nlargest, then sort them in decreasing order
    return sorted(heapq.nlargest(k, arr), reverse=True)

# Example usage:
arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(k_largest_elements(arr, k))  # Output: [50, 30, 23]
