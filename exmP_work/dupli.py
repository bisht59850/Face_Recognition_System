# arr=[1,2,3,4,5,2,3,4]

# for i in range(0,len(arr)):
#     for j in range (i+1,len(arr)):
#         if arr[i]==arr[j]:
#             print(arr[i])         


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]  # Unsorted array
bubble_sort(arr)
print("Sorted array:", arr)
