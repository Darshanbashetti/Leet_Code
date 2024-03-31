# Input

# Size of array: 6
# Enter the elements: 2 3 4 5 6 7
# Enter the index from where you want your array to rotate : 3

#  Output
# Array:
# 2 3 4 5 6 7
# New Array:
# 5 6 7 2 3 4

# N=int(input("Size : "))
# array = []
# result=[]
# for i in range(1,N+1):
#     array.append(input())
# rotate=int(input("Rotaing input : "))

# for i in array:
#     if i==array[rotate]:


def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

# Test the function
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
print("Original array:", arr)
arr = rotateArray(arr, n, d)
print("Array rotated by", d, "elements:", arr)
