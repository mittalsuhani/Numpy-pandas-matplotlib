import numpy as np
# Broadcasting in numpy arrays
arr = np.array([1, 2, 3, 4, 5])
result = arr ** 2  # Vectorized operation
print(result)  # Output: [1 4 9 16 25]

arr = np.array([1, 2, 3, 4, 5])
result = arr + 10  # Broadcasting: 10 is added to all elements
print(result)  # Output: [11 12 13 14 15]

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])
result = arr1 + arr2  # Element-wise addition
print(result)  # Output: [11 22 33]

#built in functions in numpy arrays

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))  # Output: 15
print(np.mean(arr))  # Output: 3.0
print(np.max(arr))  # Output: 5
print(np.min(arr))  # Output: 1
print(np.std(arr))  # Output: 1.4142135623730951 (standard deviation)
print(np.exp(arr))  # Output: [ 2.71828183  7.3890561  20.08553692 54.59815003 148.4131591] (exponential of each element)
print(np.log(arr))  # Output: [0.  0.69314718 1.09861229 1.38629436 1.60943791] (natural logarithm of each element)  
