# _Python for Scientific Data Analysis_

## Homework - Week 4 (continuing from Week 3)

### 4. Performing SVD (in class)

Consider the matrix ...

np.array([[1,2,3],[4,5,6],[7,8,9]])

* What happens when you try to invert this matrix directly?  Why? How could you have determined this outcome ahead of time?

* Use SVD to decompose this matrix.  Based on the singular values, where should you truncate $\Sigma$ (i.e. which ``rcond`` value)?

* Given $\Sigma$ what is the "effective" rank of the (decomposed) matrix?


### 5. Truncated SVD (in class)

Go back to the 91x91 matrix filled with random numbers.  

* Regenerate this matrix as ``aaa=np.random.rand(91,91)``
* Compute the rank of this matrix
* Re-compute the rank of this matrix if you first decompose it by SVD, truncate terms in $\Sigma$ with ``rcond < 1e-2`` and then re-compose it.
* Compute the variance treating the original matrix aaa as $\bar{x}$ and the re-composed matrix as $x$ and flattening both matrices into 1-D vectors.

### 6. Image Denoising with SVD (in class?)


Run ``svd_image.py``, which adds salt-and-pepper noise to the image given in the lecture.   

Plot the singular values for the default noise level.

For the nominal level of default noise for nlevel's default value, what number of singular values do you need to keep in order to reduce this noise (at the expense of some image quality)?


Try the same routine but on one of the other images in the directory (recommendation: the cat one is the easiest).   How does the plot of singular values differ?

