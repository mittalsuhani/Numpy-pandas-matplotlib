#indexing in numpy arrays
import numpy as np
arr = np.array([10, 20, 30, 40])
print(arr[0])  # 10
print(arr[-1]) # 40

#slicing in numpy arrays
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])  # [20 30 40] (slice from index 1 to 3)
print(arr[:3])   # [10 20 30] (first 3 elements)
print(arr[::2])  # [10 30 50] (every 2nd element)

#fancy indexing in numpy arrays
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])  # [10 30 50] (elements at indices 0, 2, and 4)

#boolean masking in numpy arrays
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
print(arr[mask])  # [30 40 50] (elements greater than 25)           

#axes in numpy arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, :])  # [1 2 3] (first row)
print(arr[:, 1])  # [2 5 8] (second column)
print(np.sum(arr, axis=0))  # Sum along rows (down each column)
print(np.sum(arr, axis=1))  # Sum along columns (across each row)

#indexing in multi-dimensional arrays
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr[1, 2])  # 60 (element at row 1, column 2)
print(arr[0:2, 1:3])  # [[20 30], [50 60]] (slice of the array) 

arr3D = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])

# Output of arr3D.shape is → (depth, rows, columns)
print(arr3D.shape) 

# First sheet, second row, third column
print(arr3D[0, 1, 2])  

print(arr3D[:, 0, :])   # Get the first row from both sheets


#data types in numpy arrays
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr)  # [1. 2. 3.]
print(arr.dtype)  # float64

arr = np.array([1, 2, 3], dtype=np.int32)
print(arr)  # [1 2 3]
print(arr.dtype)  # int32

arr = np.array([{'a': 1}, [1, 2, 3], 'hello'], dtype=object)
print(arr)  # [{'a': 1} list([1, 2, 3]) 'hello']
print(arr.dtype)  # object      

arr = np.array(['apple', 'banana', 'cherry'], dtype='U10')  # Unicode string array
print(arr)  # ['apple' 'banana' 'cherry']
print(arr.dtype)  # <U10 (Unicode string of max length 10)

