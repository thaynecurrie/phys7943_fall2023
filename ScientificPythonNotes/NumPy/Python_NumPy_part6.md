## Section 6: More Linear Algebra with NumPy and SciPy

### Singular Value Decomposition

Singular value decomposition is another ultra-powerful linear algebra operation.   For my research, it becomes especially powerful in cases where the data are noisy, such that a full matrix inversion tends to amplify noise (which, you know, is bad).   Because we live in the real world, _all_ data are noisy to some level, sometimes at a level that matters. Hence SVD.

SVD decomposes a matrix of $M$ rows and $N$ into the product of three matrices: the left singular vector $U$, the singular values $\Sigma$, and a right singular vector $V^{T}$:

$\textbf{A}$ = $\textbf{U}$ ${\Sigma}$ $\textbf{V}$$^{T}$

Note that the dimensions of each of these matrices is different: $U$ has dimensions of $MxM$ (i.e. a square matrix equal to the number of rows), the singular values $\Sigma$ have $MxN$ dimensions, and the right singular vector $V^{T}$ has $NxN$ dimensions.

In Numpy, the function to do SVD is ``np.linalg.svd``, which returns a 3-element tuple of NumPy arrays.  E.g. 

```
aaa=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])

aaa.shape
#(5,4)

U,s,Vt=np.linalg.svd(aaa)

S=np.zeros(np.shape(aaa)) ##THIS IS IMPORTANT!
np.fill_diagonal(S,s)

#Array values

#U
#array([[-0.09654784, -0.76855612,  0.60361934,  0.11849959,  0.14697464],
       [-0.24551564, -0.4896142 , -0.58187858, -0.58473646,  0.13964448],
       [-0.39448345, -0.21067228, -0.45158207,  0.7625265 , -0.12094203],
       [-0.54345125,  0.06826963,  0.23432255, -0.24484197, -0.76494794],
       [-0.69241905,  0.34721155,  0.19551877, -0.05144765,  0.59927085]])
       
#S
#array([[3.86226568e+01, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
       [0.00000000e+00, 2.07132307e+00, 0.00000000e+00, 0.00000000e+00],
       [0.00000000e+00, 0.00000000e+00, 7.60977226e-16, 0.00000000e+00],
       [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 3.86063773e-16]])
       
#Vt
#array([[-0.44301884, -0.47987252, -0.51672621, -0.55357989],
       [ 0.70974242,  0.26404992, -0.18164258, -0.62733508],
       [-0.03307776, -0.36339946,  0.82603221, -0.42955499],
       [ 0.54672284, -0.75361849, -0.13293153,  0.33982718]])
       
       
       
#dimensionality

U.shape
#(5,5)

S.shape
#(5,4)

Vt.shape
#(4,4)
```

In the above example, note the cautions about the singular value matrix, $s$.  What np.linalg.svd actually returns for $s$ is a 1-D vector of singular values (my guess is that this is for speed/memory issues). 

So, caution: $\Sigma$ is a diagonal matrix with these values, but the matrix itself is 2-D (the off-diagonal elements are zero).  To get the full middle matrix you have to create another array equal in dimensionality to the original matrix, set all elements originally to zero, and then fill the diagonals with $s$.  

We are going to stop at this point with SVDs, but do know they will become useful when trying to solve linear equations/least squares problems.


### Eigendecomposition

Another ultra-powerful linear algebra tool in NumPy and SciPy is _**eigendecomposition**_.   Don't know what this is?  Sure you've heard of it, because it is closely related to both SVD and to this magical thing called _principal component analysis_ which we will get to later in the course.  

Eigendecomposition works for square matrices.   Like SVD, it often crops up with correlation or covariance matrices (more on that later).   Every square matrix of dimensions $M x M$ has $M$ eigenvalues (scalars) and $M$ corresponding eigenvectors.  Eigendecomposition then computes these scalar-vector pairs.   

The main eigenvalue equation is very simple:

$\textbf{A}$$\textbf{v}$=$\lambda$$\textbf{v}$.   To be clear this is not saying that the matrix $A$ is the same thing as a scalar $\lambda$.  Rather, the effect or consequence of the matrix operating on the vector is the same as the effect of the scalar operating on that same vector.

So how can we find eigenvalues?   Thankfully, NumPy makes this very easy with ``np.linalg.eig``.  E.g.

```
matrix=np.array([[1,2],[3,4]])
evals,evecs=np.linalg.eig(matrix)

evals
#array([-0.37228132,  5.37228132])

evecs
#array([[-0.82456484, -0.41597356],
       [ 0.56576746, -0.90937671]])
```

And we can do the same thing with SciPy

```
from scipy import linalg
matrix=np.array([[1,2],[3,4]])
evals,evecs=linalg.eig(matrix)

evals
#array([-0.37228132,  5.37228132])

evecs
#array([[-0.82456484, -0.41597356],
       [ 0.56576746, -0.90937671]])

```

Okay fine, we can compute eigenvalues and eigenvectors.  So?  We gain a bit more insight if we rearrange the eigenvalue equation:

$\textbf{A}$$\textbf{v}$=$\lambda$$\textbf{v}$

$\textbf{A}$$\textbf{v}$-$\lambda$$\textbf{v}$=0

($\textbf{A}$-$\lambda$$\textbf{I}$)$\textbf{v}$=0

Note the imposition of the identity matrix $\textbf{I}$ (A matrix minus a scalar is not a thing/wrong dimensionality: we have to operate element-wise).  

And then ...

$\tilde{\textbf{A}}$ = $\textbf{A}$-$\lambda$$\textbf{I}$, so

$\tilde{\textbf{A}}$$\textbf{v}$ = 0 

In other words, the eigenvector is in the nullspace of the matrix shifted by its eigenvalue.  A matrix shifted by its eigenvalue is singular, because only singular matrices have non-trivial (e.g. v=0) null space.  Because singular matrices have determinants of zero, |$\textbf{A}$-$\lambda$$\textbf{I}$| =0.   I.e. we shift a matrix by its (unknown) eigenvalue $\lambda$, set its determinant to zero and solve for $\lambda$.   For the case of a simple 2x2 matrix with elements $\left[ {\begin{array}{cc}
   a & b \\
   c & d \\
  \end{array} } \right]$, shifting by eigenvalues $\lambda$ leads to the equation:
  
  $\left[ {\begin{array}{cc}
   a & b \\
   c & d \\
  \end{array} } \right]$ - $\lambda \left[ {\begin{array}{cc}
   1 & 0 \\
   0 & 1 \\
  \end{array} } \right]$, or $\lambda^{2} - (a+d)\lambda + (ad-bc)$ = 0.   I.e. this is a second order polynomial equation with thus two solutions.  A 3x3 matrix? The leading term is $\lambda^{3}$ and so on.  In other words, the characteristic polynomial of an $M$x$M$ matrix will have $\lambda^{M}$ term and a $M$x$M$ matrix will have $M$ eigenvalues.
  
Now, so far this seems a lot like SVD.   We have decomposed a matrix and get back eigenvalues and eigenvectors.  The power with both SVD and eigendecomposition comes later because we can make Python _truncate_ these matrices to filter out noise (or in more jargony language, filter out the components that do not explain much of the variance we see).   Look for a section on PCA to describe this.

