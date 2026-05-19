#comparing speeds between python lists and numpy arrays

import numpy as np
import time
list1 = list(range(1000000))
list2=list(range(1000000))
array1=np.array(list1)  
array2=np.array(list2)

start_time = time.time()
result_list = [x + y for x, y in zip(list1, list2)]     
end_time = time.time()
print("Time taken for list addition: ", end_time - start_time)

start_time = time.time()
result_array = array1 + array2
end_time = time.time()
print("Time taken for array addition: ", end_time - start_time)



#creating numpy arrays
array1 = np.array([1, 2, 3, 4, 5])
print("Array 1: ", array1)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2: \n", array2)

#array operations
array3 = array1 * 2
print("Array 3 (Array 1 multiplied by 2): ", array3)

array4 = array1 + array3
print("Array 4 (Array 1 + Array 3): ", array4)

#array slicing
print("Slicing Array 2 (first row): ", array2[0])
print("Slicing Array 2 (second column): ", array2[:, 1])

#array functions
mean_value = np.mean(array1)
print("Mean of Array 1: ", mean_value)
std_value = np.std(array1)
print("Standard Deviation of Array 1: ", std_value)

np.zeros((3, 3))  #creates a 3x3 array filled with zeros
np.ones((2, 4))   #creates a 2x4 array filled with ones
np.eye(4)         #creates a 4x4 identity matrix
print("Zeros Array:\n", np.zeros((3, 3)))
print("Ones Array:\n", np.ones((2, 4)))
print("Identity Array:\n", np.eye(4))

np.arange(1, 10, 2) # [1, 3, 5, 7, 9] (like range)
np.linspace(0, 1, 5) # [0. 0.25 0.5 0.75 1.] (evenly spaced)
print("Arange Array: ", np.arange(1, 10, 2))
print("Linspace Array: ", np.linspace(0, 1, 5)) 

#array properties

arr = np.array([[10, 20, 30], [40, 50, 60]])
 
print("Shape:", arr.shape)   # (2, 3) → 2 rows, 3 columns
print("Size:", arr.size)     # 6 → total elements
print("Dimensions:", arr.ndim) # 2 → 2D array
print("Data type:", arr.dtype) # int64 (or int32 on Windows)

#changing data type of numpy array
arr = np.array([1, 2, 3], dtype=np.float32)  # Explicit type
print(arr.dtype)  # float32
 
arr_int = arr.astype(np.int32)  # Convert float to int
print(arr_int)  # [1 2 3]

#reshaping arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original shape:", arr.shape)  # (2, 3)   
reshaped_arr = arr.reshape(3, 2)  # Reshape to 3 rows, 2 columns
print("Reshaped array:\n", reshaped_arr)
