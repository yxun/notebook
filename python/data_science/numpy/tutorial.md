
### Basics concepts

- ndarray(numpy.array) : homogeneous multidimensional array
- axis : dimension
- ndarray.ndim : the number of axes(dimensions) of the array
- ndarray.shape : the dimension of the array. a tuple of integers indicating the size of the array in each dimension.
- ndarray.size : the total number of elements of the array.
- ndarray.dtype : an object describing the type of the elements in the array.
- ndarray.itemsize : the size in bytes of each element of the array.
- ndarray.data : the buffer containing the actual elements of the array.

```python
import numpy as np

a = np.arange(15).reshape(3,5)
a.dtype.name

a = np.array([2,3,4])
c = np.array([[1,2], [3,4]], dtype=complex)
```

### Array creation
- np.zeros : creates an array full of zeros
- np.ones : creates an array full of ones
- np.empty : creates an array whose initial content is random and depends on the state of the memory.
- By default, the dtype is float64
- np.arange : creates a sequences of numbers.
- np.linspace : return evenly spaced numbers over a specified interval.

```python
import numpy as np

np.arange(6)                # 1d array
np.arange(12).reshape(4,3)  # 2d array
np.arange(24).reshape(2,3,4)    # 3d array

np.zeros((3,4))
np.ones((2,3,4), dtype=np.int16)
np.empty((2,3))
np.arange(10,30,5)
np.arange(0, 2, 0.3)

```

### Printing arrays
- the last axis is printed from left to right
- the second-to-last is printed from top to bottom
- the rest are also printed from top to bottom, with each slice separated from the next by an empty line
- If an array is too large to be printed, Numpy skips the central part and only prints the corners

To force Numpy to print the entire array:
```python
import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
```

### Basic Operations
- Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
- The product operator * operates elementwise. The matrix product can be performed using the @ operator or the dot function or method
- +=, *= and so on modify an array in place

```python
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)
c = a-b

b**2

10*np.sin(a)

a<35

a * b

a @ b

a.dot(b)

a *= 3

a.sum()

b = np.arange(12).reshape(3,4)
b.sum(axis=0)

```

### Universal Functions
ufunc operate elementwise. 

all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj,
corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, lexsort, max, maximum, mean,
median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var,
vdot, vectorize, where

### Indexing, Slicing and Iterating
One-dimensional arrays like lists in Python.
Multidimensional arrays can have one index per axis. When fewer indices are provided, the missing indices are considered complete slices.
The dots (...) represent as many colons as needed to produce a complete indexing tuple.
x[1,2,...] is equivalent to x[1,2,:,:]

Iterating over multidimensional arrays is done with respect to the first axis.
If one wants to perform an operation on each element in the array, one can use the flat attribute.
for element in b.flat:
    print(element)

### Shape Manipulation
The following three return a modified array, not change the original array.

a.ravel()       # returns the array, flattened
a.reshape(x,y)  # returns the array with a modified shape
a.T             # returns the array, transposed 

The reshape function returns its argument with a modified shape. The ndarray.resize method modifies the array itself.

If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated.

#### Stacking together different arrays

```python
import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random(2,2))
b = np.floor(10*np.random.random(2,2))

np.vstack(a,b)
np.hstack(a,b)

np.column_stack((a,b))

a = np.array([4., 2.])
b = np.array([3., 8.])

np.column_stack((a,b))
np.hstack((a,b))

a[:, newaxis]

np.column_stack((a[:,newaxis], b[:,newaxis]))
np.hstack((a[:,newaxis], b[:,newaxis]))

```

In general, for arrays with more than two dimensions, hstack stacks along their second axes, vstack stacks along their first axes, and concatenate allows for an optional arguments giving the number of the axis.

#### Splitting one array into several smaller ones
Use hsplit, split an array along its horizontal axis. vsplit splits along the vertical axis, and array_split allows one to specify along which axis to split.

```python
import numpy as np

a = np.floor(10*np.random.random((2,12)))

np.hsplit(a,3)      # Split a into 3
np.hsplit(a, (3,4)) # Split a into 3, first part after the third column, second part the fourth column, thrid part after the fourth column

```

#### Copies and Views
The view method creates a new array object that looks at the same data.
Slicing an array returns a view of it.

```
c = a.view()
c is a
False

c.base is a
True

c.flags.owndata
False

c.shape = 2,6
a.shape     # a's shape doesn't change
[3,4]

c[0,4] = [1,2,3,4]  # a's data changes

```

#### Deep Copy
The copy method makes a complete copy of the array and its data.

### Functions and Methods Overview

- Array Creation: arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
- Conversions: ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
- Manipulations: array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
- Questions: all, any, nonzero, where
- Ordering: argmax, argmin, argsort, max, min, ptp, searchsorted, sort
- Operations: choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum
- Basic Statistics: cov, mean, std, var
- Basic Linear Algebra: cross, dot, outer, linalg.svd, vdot

#### Broadcasting

#### Fancy indexing and index tricks
Arrays can be indexed by arrays of integers and arrays of booleans. When the indexed array a is multidimensional, a single array of indices refers to the first dimension of a.


```
a = np.arange(12) ** 2
i = np.array([1,1,3,8,5])
a[i]

j = np.array([3,4],[9,7])
a[j]

```

Indexing with arrays as a target to assign to

```
a = np.arange(5)
a[[1,3,4]] = 0

```

Example: Use boolean indexing to generate an image of the Mandelbrot set

```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot( h, w, maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime

plt.imshow(mandelbrot(400, 400))
plt.show()

```

#### The ix_() function


### Linear Algebra

```python
import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)

a.transpose()

np.linalg.inv(a)

u = np.eye(2)   # unit 2x2 matrix; "eye" represents "I", or 1

j = np.array([[0.0, -1.0], [1.0, 0.0]])

j @ j   # matrix product

np.trace(u)

y = np.array([[5.], [7.]])
np.linalg.solve(a, y)

np.linalg.eig(j)

```

### Tricks and Tips

#### "Automatic" Reshaping 
To change the dimensions of an array, you can omit one of the sizes which will then be deduced automatically.

```
a = np.arange(30)
a.shape = 2, -1, 3  # -1 means "whatever is needed"
a.shape

```

#### Vector Stacking 

```
x = np.arange(0, 10, 2)
y = np.arange(5)
m = np.vstack([x,y])
xy = np.hstack([x,y])

```

#### Histograms

```python
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=50, density=1) # matplotlib version plot
plt.show()

# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, desity=True)   # Numpy vresion, no plot
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()

```

