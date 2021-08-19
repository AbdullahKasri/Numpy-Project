import pandas as pd
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.average(a, axis = 0)
c = np.var(a, axis = 0)
d = np.std(a, axis = 0)
e = np.max(a, axis = 1)
f = np.min(a, axis = 1)
h = np.sum(a, axis = 1)



print("Array: ", a)
print("Mean: ", b)
print("Variance: ", c)
print("Standard Deviation: ", d)
print("Maximum: ", e)
print("Minimum: ", f)
print("Total: ", h)
