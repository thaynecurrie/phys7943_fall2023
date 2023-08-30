# _Python for Scientific Data Analysis_

## Homework - Week 2

## Monday

### 1. Dictionaries

Use three defined dictionaries with the following entries -- 1. city + country abbreviation, 2. country abbreviation + skyscraper, 3. skyscraper + height.   

Assume the following building heights (i.e. this will be dictionary number 3):
 Petronas Towers - 1483 ft
 WTC - 1776 ft
 Eiffel Tower - 1083 ft
 
 Write a for-loop that prints out the country, abbreviation, city, building, and height converted to au (assume 1 foot = 2.0375e-12 au):
 
 ```
The tallest building in the city of Paris, FR is the Eiffel Tower with a height of 2.207e-09 au
The tallest building in the city of New York, USA is the WTC with a height of 3.619e-09 au
The tallest building in the city of Kuala Lumpur, MY is the Petronas Towers with a height of 3.022e-09 au
 ```
 
 
### 2. Lists, Arrays, Loops and Type Conversions (in-class):

Start with a list 4 elements long, including a mix of floating point numbers and integers: $\pi$, e, 3.1 and 5.

Remove 3.1 using the ``remove`` function and array indexing.  

Append Euler's gamma constant to the list

Write a line of code that prints out ``a``, repeated 3 times

Write a line of code that prints out each element of ``a`` multiplied by 3

Write a for-loop that prints out each element of ``a`` multiplied by 3

### 3. Slicing (in-class)

Consider the array:

``a=[2,3,5,6,8,9,10]``

Use slicing to produce the following:

 ``[2,5,8,10]``
 
 ``[6,8,9]``
 
 ``[10, 9, 8, 6, 5, 3, 2]``
 
### 4. Slicing (in-class)
 
 Convert ``a`` to an array and then use conditional/boolean slicing to print out
 
 ``array([ 6,  8,  9, 10])``
 
 
 ``array([ 2,  8,  9, 10])``


### 5. Sequence Function (in-class)

Consider three lists -- episode=['Eegah','Deathstalker','Space Mutiny']; line=["Watch out for Snakes","He's Batman","Big McLarge Huge"] ; season = [5,7,8]

Use the ``zip`` sequence function in a for-loop to produce the following output:

```
The best line of the episode Eegah in season 5 was "Watch out for Snakes" 
The best line of the episode Deathstalker in season 7 was "He's Batman" 
The best line of the episode Space Mutiny in season 8 was "Big McLarge Huge" 
```

### 6. Sequence Functions
 
 Consider the example shown in the data struct part 3 notes of the list comprehension for four stars wth different names ``HIP 99770, AF Lep, HR 8799, Vega.``.  It used ``zip`` to advance each element of starname, spectype, starmag, and dstar 
 
 Now, add the use of ``enumerate`` to write a for-loop printing out the number of the star in the list and an indexed version of``absmag`` at each interation and then print the full array of ``absmag`` outside of the for-loop.  Your answer should look like this when you run the code:
 
```
The absolute magnitude of star number 1 with name HIP 99770 with spectral type A5V is 1.850
The absolute magnitude of star number 2 with name AF Lep with spectral type F8V is 4.159
The absolute magnitude of star number 3 with name HR 8799 with spectral type F0V is 2.923
The absolute magnitude of star number 4 with name Vega with spectral type A0V is 0.568
```
as before, and then

```
[1.84989488 4.15932603 2.92251889 0.56754637]
```
outside of the loop.


 
 
### 7. List Comprehensions
 
 Consider a list ``vals=[.1,2,.4,3]``
 
 Write a list comprehension returning a variable ``vals2`` which equals ``[6,9]`` (i.e. vals[1] and vals[3] each times 3) using the value of 1/x versus 1/x$^{2}$ for each element ``x`` of ``vals`` as the conditional.
 

 
## Wednesday

### 8. NumPy Array Creation (in class)

Create a 4x3 dimension NumPy array filled with random numbers called ``multi_array``

Use a NumPy Function and array slicing to create a second array called ``multi_array2`` with the same dimensions as ``multi_array`` but with the 0th column of the array filled with ones (``1's``).


### 9. NumPy Slicing with Boolean Indexing

Read in file ``spectrum_oct17_adi.dat`` from the notes using ``np.loadtxt``.   It has columns of wavelength, flux density, uncertainty (flux density), and signal-to-noise ratio.   

 Use the ``np.where`` statement to replace the values for uncertainty (flux density) by ``-9`` for rows where the signal-to-noise ratio is less than 5.

Save a new file with columns of wavelength, flux density, uncertainty (flux density), and signal-to-noise ratio, where you have updated the uncertainty values.

### 10. Array Reshaping (In Class)

Another trick we can do with NumPy is the function ``linspace`` (i.e. ``np.linspace``), which returns evenly spaced numbers over a specified interval.   ``linspace`` gets very useful when we want to do looping or interpolation.

Read up on it here: [https://numpy.org/doc/stable/reference/generated/numpy.linspace.html]()

Create one array using ``np.linspace`` with 100 values between 5 and 10: i.e. ``np.linspace(5,10,num=100)``.  

Then convert this row vector to a column vector called ``a_col`` using ``reshape``.  

Then convert ``a_col`` into a 2-D array called ``a_2d`` (i.e. a matrix) with 20 rows.

Then use ``transpose`` to convert the 2-D array into a new one called ``a_2dt`` that has 20 columns.

Then convert it back to a row vector called ``a_flat`` using ``flatten``.



### 11. (Grad Students Only; Extra Credit for Undergrads) 

In addition to ``np.loadtxt`` there's a key NumPy function called ``np.genfromtxt``, which is supposed to treat missing table entries.  However, sometimes it fails to parse missing entries correctly (search StackOverFlow topics on this for some examples).  So when presented with a table containing missing values, sometimes we have to improvise.

Load the file ``test.csv``

**Without using a for-loop** ...

 * clean missing entries for semimajor axis (i.e. entries that just have a `` ''`` ... set them to a negative number)
 
 * for entries that do NOT have a missing semimajor axis, compute the median semimajor axis for planets discovered using ... a) Imaging, b) Radial Velocity, and c) Transit.

Hints:
 
 * you will need to use ``np.where`` multiple times;       
 
 * after cleaning the data, you will need use ``astype`` to convert key variables to floating point else you may get a ``TypeError: '>' not supported between instances of 'numpy.ndarray' and 'int'`` error

