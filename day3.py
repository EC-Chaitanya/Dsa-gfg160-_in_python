# to reverse an array
# in place
def reverse_a( arr):
    a = 0
    b = len(arr)-1
    while a < b:
        arr[a], arr[b] = arr[b], arr[a]
        a += 1
        b -= 1
        # print(arr[i])
arr = [1, 2,  3, 4, 5, 6, 7, 8]
reverse_a(arr)   
print(arr)     
