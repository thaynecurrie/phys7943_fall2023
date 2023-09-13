import numpy as np
import numpy.random as rnd

import matplotlib.pyplot as plt

def runme(npca=5,plotrelpc=True,plotorigvspc=True):

#####Setting Up
 ndim = 10
 mu = np.array([3]+np.random.rand(ndim)) # Mean
 sigma=np.full((ndim,ndim),5+np.random.rand(ndim*ndim).reshape(ndim,ndim))

#some trickery to adjust the relative PCs to an interesting range of values
 sigarr=5+np.arange(0,ndim)*0.5
 sigarr[0:2]=np.array([15,7.5]) 
 np.fill_diagonal(sigma,sigarr)

# print("Mu ", mu.shape)
# print("Sigma ", sigma.shape)
 
 # Create 1000 samples using mean and sigma
 org_data = rnd.multivariate_normal(mu, sigma, size=(1000))
 print("Data shape ", org_data.shape) 


 ##### Step 1 -  Subtract mean from data
 mean = np.mean(org_data, axis= 0)
# print("Mean ", mean.shape)

 mean_data = org_data - mean
# print("Data after subtracting mean ", org_data.shape, "\n")


 #cov = np.cov(mean_data.T)
 #cov = np.cov(mean_data,rowvar=False)

#### Step 2 - Computing the Covariance Matrix
 cov=np.matmul(mean_data.T,mean_data)

 #print("Covariance matrix ", cov.shape, "\n")


#### Step 3 - Eigendecomposition
 eig_val, eig_vec = np.linalg.eigh(cov)

# print("Eigen vectors ", eig_vec.shape)
# print("Eigen values ", eig_val.shape, "\n")
 
 
#### Step 4 - Sort the Eigenvalues and Eigenvectors, large to small
 indices = np.argsort(eig_val)[::-1]

 eig_val = eig_val[indices]
 eig_vec = eig_vec[:,indices]


###some analysis 
 # Get explained variance
 sum_eig_val = np.sum(eig_val)
 explained_variance = eig_val/ sum_eig_val

 print("Explained variance ", explained_variance)
 cumulative_variance = np.cumsum(explained_variance)
 print("Cumulative variance ", cumulative_variance)

 if plotrelpc: 
  # Plot explained variance
  plt.plot(np.arange(0, len(explained_variance), 1), cumulative_variance,marker='o')
  plt.title("Explained variance vs number of components")
  plt.xlabel("Number of components")
  plt.ylabel("Explained variance")
  plt.show()

####end some analysis
 

#### Step 5a - Select number of PCs to compute ... 
 ## We will retain npca components
 n_comp = npca
 eig_vec = eig_vec[:,:n_comp]
 eig_val=eig_val[:n_comp]
# print(eig_vec.shape)


#### Step 5b - Compute the PCs
 # Take transpose of eigen vectors with data --> get PCs
 pca_data = mean_data.dot(eig_vec)

# print("Transformed data ", pca_data.shape)



#### Analysis 
 # Plot data


 if plotorigvspc:
  fig, ax = plt.subplots(1,3, figsize= (12,8))
  # Plot original data
  ax[0].scatter(org_data[:,0], org_data[:,1], color='blue', marker='.')
  
  # Plot data after subtracting mean from data
  ax[1].scatter(mean_data[:,0], mean_data[:,1], color='red', marker='.')
  
  # Plot data after subtracting mean from data
  ax[2].scatter(pca_data[:,0], pca_data[:,1], color='red', marker='.')
  
  # Set title
  ax[0].set_title("Original data")
  ax[1].set_title("Original data after subtracting mean")
  ax[2].set_title("Transformed data, PC="+str(npca))
  
  # Set x ticks
  ax[0].set_xticks(np.arange(-8, 1, 8))
  ax[1].set_xticks(np.arange(-8, 1, 8))
  ax[2].set_xticks(np.arange(-8, 1, 8))
  
  # Set grid to 'on'
  ax[0].grid('on')
  ax[1].grid('on')
  ax[2].grid('on')
  
  #major_axis = eig_vec[:,0].flatten()
  xmin = np.amin(pca_data[:,0])
  xmax = np.amax(pca_data[:,0])
  ymin = np.amin(pca_data[:,1])
  ymax = np.amax(pca_data[:,1])
  
  plt.show()
  plt.close('all')


#### Step 6 - Reconstruct Original Data from PCs
 # Reverse PCA transformation
 recon_data = pca_data.dot(eig_vec.T) + mean
 
#print(recon_data.shape)


 fig, ax = plt.subplots(1,3, figsize= (12, 8))
 ax[0].scatter(org_data[:,0], org_data[:,1], color='blue', marker='.')
 xl=ax[0].get_xlim()
 yl=ax[0].get_ylim()

 ax[1].scatter(recon_data[:,0], recon_data[:,1], color='red', marker='.')
 ax[1].set_xlim(xl)
 ax[1].set_ylim(yl)

 ax[2].scatter(org_data[:,0]-recon_data[:,0], org_data[:,1]-recon_data[:,1], color='green', marker='.')
 ax[2].set_xlim(xl)
 ax[2].set_ylim(yl)

 ax[0].set_title("Original data")
 ax[1].set_title("Reconstructed data, PC="+str(npca))
 ax[2].set_title("Original-Reconstructed data,PC="+str(npca))
 ax[0].grid('on')
 ax[1].grid('on')
 ax[2].grid('on')
 plt.show()
 plt.close('all')
 
