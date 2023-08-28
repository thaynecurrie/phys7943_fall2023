# _Python for Scientific Data Analysis_

# NumPy/SciPy

## Section 2: Array Arithmetic and Universal Functions

### Arithmetic

As stated in the previous section, arrays are important because they enable you to express batch operations on data

Beyond the simple example given before, here are some examples of array arithmetic:

```
arr = np.array([[1., 2., 3.], [4., 5., 6.]])

arr

#array([[ 1., 2., 3.],

arr * arr

#array([[ 1., 4., 9.],

arr - arr
#array([[ 0., 0., 0.],
```

Arithmetic operations with scalars propagate the scalar argument to each element in

```
1 / arr

#array([[ 1. , 0.5 , 0.3333],

arr ** 0.5

#array([[ 1. , 1.4142, 1.7321],
```

Comparisons between arrays of the same size yield boolean arrays:

```
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr2

arr2 > arr
#array([[False, True, False],

```

Operations between arrays of different sizes is called _broadcasting_: we will discuss that later.

### Universal Functions

NumPy contains _universal functions_ that perform vectorized operaitons on NumPy arrays. 

_unary_ universal functions perform element-wise transformations and are called as ``np.functionname(array)``.  E.g. ``np.exp(array)``, ``np.sqrt(array)``, ``np.floor(array)``.   Here are some examples:

| Function| Description |
| -------| ----------- | 
|abs, fabs | Compute the absolute value element-wise for integer, floating-point, or complex values

_binary_ universal functions two two arrays and return a single array as a result.  They are called as ``np.functionname(array1,array2)``.  Here are some examples:

| Function| Description |
| -------| ----------- | 
|add |Add corresponding elements in arrays
|greater, greater\_equal,less, less\_equal,equal, not_equal|Perform element-wise comparison, yielding boolean array (equivalent to infix operators >, >=, <, <=, ==, !=)

Some ufuncs can return multiple arrays -- e.g. ``np.modf`` which returns the fractional and integral parts of a floating point array.   But these are uncommon.
