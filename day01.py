'''Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.'''

def second_largest(arr):
    if len(arr) < 2:
        return -1
    
    max_element = second_max = float('-inf')
    
    for num in arr:
        if num > max_element:
            second_max = max_element
            max_element = num
        elif num > second_max and num != max_element:
            second_max = num
    
    if second_max == float('-inf'):
        return -1
    else:
        return second_max
