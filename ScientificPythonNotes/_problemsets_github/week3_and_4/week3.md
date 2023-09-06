# _Python for Scientific Data Analysis_

## Homework - Week 3

### 1. Broadcasting

Consider two arrays

```
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
```
and

```
arr2=np.array([79,89,99])
```

write a line(s) of code that ...

a) replaces each column of arr1 by arr2

b) replaces each row of arr1 by arr2

c) replaces only the 2nd and 3rd column of arr by arr2


### 2. Repeating Array Elements

take the array a=np.array([10,20,30,40,50]) ...

part 1

* use ``np.tile`` to repeat this entire array 5 times
* use ``reshape`` to convert this array into a 2-D matrix.   With the ``reshape`` command use i) the length of ``a``  (i.e. ``len(a)``) and ii) ``-1`` to do the reshaping instead of hardcoding the dimensions.
* take the determinant of this matrix and report the result.  

part 2

* now take the determinant of the matrix 
 ``a=np.array([[1,2.333,-4],[-4,-3,-.001],[-.2,5.3,9.99]])``
 
part 3
 
* now, flatten the array in part 2:

you should get ``aflat=array([ 1,  2.333, -4, -4, -3,
       -0.001, -.2,  5.3,  9.99])``
       
use ``np.tile`` to repeat this array 
 three times and follow the steps in part 1 to compute the determinant.  Notice a pattern?
 
### 3. Solving a System of Linear Equations

Consider this system of linear equations :

8$a_{o}$ + 6$a_{1}$ - 10$a_{2}$ = 2

-4$a_{o}$ - 8$a_{1}$ + 10$a_{2}$ = 5

16$a_{o}$ + 16$a_{1}$  = -3

* Solve this system of equations with i) ``np.linalg.solve`` and ii) ``np.linalg.inv`` + ``np.dot``

* Verify that the values for $a_{o}$, $a_{1}$, and $a_{2}$ provide an exact solution (hint: verify that the lefthand side of the equation yields the righthand side).
 
 