#### A from-scratch demonstration of the eigenfaces application of PCA using NumPy
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_lfw_people

def run(numpca=150):

 faces = fetch_lfw_people(min_faces_per_person=60)
 print(faces.images.shape)
# print(faces.target_names)

#Step 1
 faces_mean=faces.data-np.mean(faces.data,axis=0)

#Step 2
 cov=np.matmul(faces_mean.T,faces_mean)

#Step 3
 eig_val,eig_vec=np.linalg.eigh(cov)

#Step 4 
 indices=np.argsort(eig_val)[::-1]
 eig_val=eig_val[indices]
 eig_vec=eig_vec[:,indices]

#Step 5
 n_comp=numpca
 eig_vec=eig_vec[:,:n_comp]
 eig_valtot=eig_val
 eig_val=eig_val[:n_comp]

 pca_components=((faces_mean).dot(eig_vec))  


### Plotting the Eigenvectors
 fig, axes = plt.subplots(3, 8, figsize=(9, 4),
                          subplot_kw={'xticks':[], 'yticks':[]},
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i, ax in enumerate(axes.flat):
     ax.imshow(eig_vec[:,i].reshape(62,47),cmap='bone')
 

 plt.show()

############


### Plotting the contribution of each PC to the total variance
 totvar=np.sum(eig_valtot)

 explained_var_ratio=eig_valtot/totvar

#Computing the Cumulative Variance of each eigenvector/PC

 cumul_sum_eigval=np.cumsum(explained_var_ratio)
 plt.bar(range(0,len(explained_var_ratio)),explained_var_ratio,alpha=0.5,align='center',label='Individual Explained Variance',color='orange' )
 plt.step(range(0,len(cumul_sum_eigval)),cumul_sum_eigval,where='mid',label='Cumulative Explained Variance',linewidth=3.0)

 plt.xlabel('number of components')
 plt.ylabel('cumulative explained variance');
 plt.xlim(-5,n_comp)
 plt.ylim(0,1.0)
 plt.tight_layout()
 plt.legend(loc='best')
 plt.show()

############
 
 
#Step 6 
 pca_inverse_transform=pca_components.dot(eig_vec.T)+np.mean(faces.data,axis=0)


#### Plotting the Real Images and PC-Projected Images
 fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
                        subplot_kw={'xticks':[], 'yticks':[]},
                        gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i in range(10):
     ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
     ax[1, i].imshow(pca_inverse_transform[i].reshape(62, 47), cmap='binary_r')
     
 ax[0, 0].set_ylabel('full-dim\ninput')
 ax[1, 0].set_ylabel(str(numpca)+'-dim\nreconstruction');

 plt.show()
