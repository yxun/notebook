
## Data types
Ref: https://numpy.org/devdocs/user/basics.types.html

The primitive types supported are tied closely to those in C:

```
np.bool
np.byte
np.ubyte
np.short
np.ushort
np.intc
np.uintc
np.int_
np.unit
np.longlong
np.ulonglong
np.half / np.float16        # Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
np.single       # Platform-defined single precision float: typically sign bit, 8 bits exponent, 23 bits mantissa
np.double       # Platform-defined double precision float: typically sign bit, 11 bits exponent, 52 bits mantissa
np.longdouble
np.csingle      # Complex number, represented by two single-precision floats (real and imaginary components)
np.cdouble      # Complex number, represented by two double-precision floats
np.clongdouble
```

Fixed-size aliases:

```
np.int8     # Byte (-128 to 127)
np.int16    # Integer (-32768 to 32767)
np.int32    # Integer (-2147483648 to 2147483647)
np.int64
np.uint8    # Unsigned integer (0 to 255)
np.uint16   # Unsigned integer (0 to 65535)
np.uint32   # Unsigned integer (0 to 4294967295)
np.uint64
np.intp     # Integer used for indexing, typically the same as ssize_t
np.uintp    # Integer large enough to hold a pointer
np.float32  
np.float64 / np.float_      # matches the builtin python float
np.complex64    # Complex number, represented by two 32-bit floats
np.complex128 / np.complex_     # matches the builtin python complex
```

Numpy numerical types are instances of dtype (data-type) objects. Advanced types are explored in section Structured arrays.

Data-types can be used as functions to convert python numbers to array scalars, python sequences of numbers to arrays of that type, or as arguments to the dtype keyword.

```python
import numpy as np
x = np.float32(1.0)
y = np.int_([1,2,4])
z = np.arange(3, dtype=np.uint8)
```

To convert the type of an array, use the .astype() method or the type itself as a function.
```python
z.astype(float)
np.int8(z)
```

To determine the type of an array, look at the dtype attribute, z.dtype

### Array Scalars
Numpy generally returns elements of arrays as array scalars (a scalar with an associated dtype). 

### Overflow Errors
The fixed size of Numpy numeric types may cause overflow errors when a value requires more memory than available in the data type. For example

```
>>> np.power(100, 8, dtype=np.int64)
10000000000000000
>>> np.power(100, 8, dtype=np.int32)
1874919424
```

Unlike Numpy, the size of Python's int is flexible.
Numpy provides numpy.iinfo and numpy.finfo to verify the minimum or maximum values of Numpy integer and floating point values.

```
>>> np.iinfo(np.int) # Bounds of the default integer on this system.
iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
>>> np.iinfo(np.int32) # Bounds of a 32-bit integer
iinfo(min=-2147483648, max=2147483647, dtype=int32)
>>> np.iinfo(np.int64) # Bounds of a 64-bit integer
iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
```

if 64-bit integers are still too small the result may be cast to a floating point number. Floating point numbers offer a larger, but inexact, range of possible values.

```
>>> np.power(100, 100, dtype=np.int64) # Incorrect even with 64-bit int
0
>>> np.power(100, 100, dtype=np.float64)
1e+200
```


## Array creation

5 general mechanisms for creating arrays:
```
1. Conversion from other Python strctures (e.g., lists, tuples)
2. Intrinsic numpy array creation objects (e.g., arange, ones, zeros,)
3. Reading arrays from disk, either from standard or custom formats
4. Creating arrays from raw bytes through the use of strings or buffers
5. Use of special library functions (e.g., random)
```

### Converting Python array_like Objects to Numpy Arrays
Use the np.array() function

### Intrinsic Numpy Array Creation
- zeros(shape) : create an array with 0 values. The default dtype is float64.
- ones(shape) : create an array with 1 values. The default dtype is float64.
- arange() : create arrys with regularly incrementing values.
- linspace() : create arrays spaced equally.
- indices()

### Reading Arrays From Disk
Standard binary formats exmaples: HDF5: h5py, FITS: Astropy
Common ASCII formats example: CSV: matplotlib, pylab, scipy

## I/O with Numpy

### Import data with genfromtxt
genfromtxt runs two main loops. The first loop converts each line of the file in a sequence of strings. The second loop converts each string to the appropriate data type. 
Arguments: delimiter, autostrip, comments, names, skip_header, skip_footer, usecols, dtype, defaultfmt, converters, missing_values, filling_values

```python
import numpy as np
from io import StringIO

data = u"1, 2, 3\n4, 5, 6"
np.genfromtxt(StringIO(data), delimiter=",")

```

## Indexing
numpy arrays support multidimensional indexing for multidimensional arrays. such as x[1,3]. 
Numpy arrays may be indexed with other arrays (or any other sequence like object that can be converted to an array such as lists, with the exception of tuples). For all cases of index arrays, what is returned is a copy of the original data, not a view as one gets for slices.


## Broadcasting




