# print("hello world")


# Question 1a
# Here's a Python function that reads a CSV file containing matric numbers and scores, computes the average and standard deviation of the scores, and returns the highest and lowest scores along with the computed values:

# import csv
# import math
# import pandas as pd
#
# def process_scores(file_path):
#     # Read the CSV file using pandas
#     df = pd.read_csv(file_path, header=None, names=["Matric Number", "Score"])
#
#     # Compute the average and standard deviation of the scores
#     average = df["Score"].mean()
#     std_dev = df["Score"].std()
#
#     # Find the highest and lowest scores
#     highest = df["Score"].max()
#     lowest = df["Score"].min()
#
#     # Return all the computed values as a dictionary
#     return {"Average": average, "Standard Deviation": std_dev, "Highest": highest, "Lowest": lowest}

# The function first reads the CSV file using pandas and stores the contents in a DataFrame called df. It then computes the average and standard deviation of the scores using the mean() and std() methods of the DataFrame, respectively. The function also finds the highest and lowest scores using the max() and min() methods of the DataFrame.
#
# Finally, the function returns a dictionary containing all the computed values. The dictionary has keys "Average", "Standard Deviation", "Highest", and "Lowest", with the corresponding computed values as the values.


# Question 1b

# Function to check if a number is prime
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# # Loop through numbers 1 to 1000 and print the primes
# for num in range(1, 1001):
#     if is_prime(num):
#         print(num)


# Question 2a

# i). To get the shape of the numpy array `a`, you can use the `shape` attribute of the array. Here's the Python code to get the shape of `a`:

# print(a.shape)

# ii). The shape of the numpy array `a` is `(3, 4)`. This means that `a` has 3 rows and 4 columns.
# ii). To square all the elements of the numpy array `a` in one single operation, you can use the `np.square()` function. Here's the Python code to square all the elements of `a`:

# a_squared = np.square(a)
# print(a_squared)
# The `np.square()` function applies the square function element-wise to the input array `a` and returns a new array containing the squared values. The resulting array `a_squared` has the same shape as the original array `a`.



# Question 2b
# i. Scalar and vector:
#
# A scalar is a single number, while a vector is an array of numbers.

# Scalars have no direction, while vectors have both magnitude (length) and direction.

# Scalars are represented as a single value, while vectors are represented as an array of values.

# Scalar operations are arithmetic operations on a single value, while vector operations are arithmetic operations performed element-wise on the corresponding elements of two vectors.



# ii. Vector and Matrix:
#
# A vector is a one-dimensional array of numbers, while a matrix is a two-dimensional array of numbers.

# Vectors can be thought of as special cases of matrices with either a single row (row vector) or a single column (column vector).

# Matrices can be used to represent linear transformations, while vectors can be thought of as representing points or directions in space.

# Vector operations (e.g., dot product, cross product) are different from matrix operations (e.g., matrix multiplication, element-wise addition).



# iii. Single precision and double precision:
#
# Single precision and double precision are two different levels of precision used to represent floating-point numbers.

# Single precision uses 32 bits to represent a floating-point number, while double precision uses 64 bits.

# Single precision can represent a smaller range of numbers and has less precision than double precision.

# Double precision is more accurate and is generally used when high precision is required, such as in scientific or engineering calculations.



# iv. Flatten and ravel:
#
# flatten() and ravel() are two numpy functions used to convert a multi-dimensional array into a one-dimensional array.

# flatten() always returns a copy of the original array, while ravel() may return a copy or a reference to the original array.

# flatten() creates a new copy of the array in memory, while ravel() does not always create a new copy.

# flatten() always returns a contiguous array, while ravel() returns a non-contiguous array if possible.

# flatten() returns a flattened copy of the array in row-major (C-style) order, while ravel() returns a flattened array in the same order as the input array.


# Question 2b
# i). 𝑥=(𝑎𝑏−2𝑎)/2𝑏
# x = (a*b - 2*a)/(2*b)


# ii). 𝑥=cube√3𝑏−𝑎𝑐/𝑐
# x = ((3*b - a*c)/c)**(1/3)


# iii). 𝑥=(−𝑏±(√𝑏^2−4𝑎𝑐))/2𝑎
# x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
# x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)




# Question 3a

# The main difference between the two arrays is their shape.
# The array `a` is a 1-dimensional array with shape `(3,)`. It contains three elements, each with the value 1.
# The array `b` is a 2-dimensional array with shape `(1,3)`. It also contains three elements, each with the value 1, but they are arranged in a single row within the array.
#
# Another way to think about it is that `a` is a vector, while `b` is a matrix with one row.
#
# Here's an example to illustrate the difference:

# import numpy as np
# a = np.array([1, 1, 1])
# b = np.array([[1, 1, 1]])
#
# print(a)
# # [1 1 1]
#
# print(b)
# # [[1 1 1]]
#
# print(a.shape)
# # (3,)
#
# print(b.shape)
# # (1, 3)


# Question 3b

# i). Create an array a with dimension 4 × 2.
# a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

# ii). Print the 1st row of a.
# print(a[0])

# iii). Print the 2nd column of a.
# print(a[:, 1])

# iv). Print every element from the 2nd row to the last row of a.
# print(a[1:])

# v). Add 100 to every element of a.
# a = a + 100
# print(a)


# Question 4a (a = np.linspace(1, 48, 48).reshape(3, 4, 4))

# i). What is the shape of `a`? Write the code to get it
# The shape of `a` is `(3, 4, 4)`. To get the shape of `a`, you can use the `shape` attribute of the NumPy array as follows:
# print(a.shape)

# ii). How many elements does `a` have? Write the code to get it
#  `a` has 48 elements. To get the number of elements in `a`, you can use the `size` attribute of the NumPy array as follows:
# print(a.size)

# iii). What is the rank of `a`? Write the code to get it
# The rank of `a` is 3. To get the rank of `a`, you can use the `ndim` attribute of the NumPy array as follows:
# print(a.ndim)

# iv). What is the data type of `a`? Write the code to get it
# The data type of `a` is float64. To get the data type of `a`, you can use the `dtype` attribute of the NumPy array as follows:
# print(a.dtype)


# Question 4b
# The Python math module and the NumPy library provide functions for mathematical operations, but there are some fundamental differences between them.
#
# 1) Data types:
# The math module is designed to work with scalar values, while NumPy is built for arrays and matrices. This means that while the math module can handle individual numbers, NumPy is designed to work with large sets of data.
#
# 2) Performance:
# NumPy is optimized for numerical operations and is generally faster than the math module when working with arrays and matrices. NumPy uses optimized C and Fortran code, making it faster than pure Python implementations.
#
# 3) Functionality:
# The math module provides a wide range of mathematical functions, including trigonometric, logarithmic, and exponential functions. NumPy provides a much larger set of mathematical functions, including linear algebra, Fourier transforms, and statistical functions.
#
# 3)Broadcasting:
# NumPy has a concept of broadcasting, which allows mathematical operations to be performed on arrays of different sizes and shapes. This can be a powerful tool for working with large sets of data. The math module doesn't support broadcasting, and operations must be performed on individual numbers.
#
# In summary, the main difference between the math module and NumPy is that the math module is designed for scalar values and provides a limited set of mathematical functions, while NumPy is designed for arrays and matrices and provides a much wider range of mathematical functions optimized for numerical operations.
