import numpy as np


def runme():


 x=np.array([[7,4,3,],[4,1,8],[6,3,5.],[8,6,1],[8,5,7]])

 meanval=np.mean(x,axis=0)
 print(meanval)
 print(x)
# exit()
 x_meaned=x-meanval

# covmat=np.cov(x_meaned,rowvar=False)

 covmat=np.matmul(x_meaned.T,x_meaned)
 eval , evec = np.linalg.eigh(covmat)

 print("Eigen vectors ", evec.shape)
 print("Eigen values ", eval.shape, "\n")

 sorted_index = np.argsort(eval)[::-1]
 eval=eval[sorted_index]
 evec=evec[:,sorted_index]

 print("Sorted Eigen vectors ", evec.shape)
 print("Sorted Eigen values ", eval.shape, "\n")

  # Take transpose of eigen vectors with data
 X_red = x_meaned.dot(evec)
 print("Transformed data ", X_red.shape)

  # Reverse PCA transformation
 X_red2 = X_red.dot(evec.T) + meanval

 print(X_red.shape)

 print(x)

 print(X_red) 

 print(X_red.shape)

 print(X_red2)

 print(evec.dot(evec.T))

def runme2():


 X =np.array([[7,4,3,],[4,1,8],[6,3,5.],[8,6,1],[8,5,7]])
 #X = np.random.randint(10,50,10).reshape(5,2) 
 X_meaned = X - np.mean(X , axis = 0)
 cov_mat = np.cov(X_meaned , rowvar = False)
 eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
 
 sorted_index = np.argsort(eigen_values)[::-1]
 
 sorted_eigenvalue = eigen_values[sorted_index]
#similarly sort the eigenvectors 
 sorted_eigenvectors = eigen_vectors[:,sorted_index]


 eigenvector_subset = sorted_eigenvectors[:,:]

 X_reduced = np.dot(eigenvector_subset.transpose(),X_meaned.transpose()).transpose()


 print((X_reduced+np.mean(X,axis=0))*eigen_values)

 print(X)

def runme3():

 import sklearn.decomposition


 X =np.array([[7,4,3,],[4,1,8],[6,3,5.],[8,6,1],[8,5,7]])
 #X = np.random.randint(10,50,10).reshape(5,2) 
 X_meaned = X - np.mean(X , axis = 0)

 pca=sklearn.decomposition.PCA()
 pca.fit(X)

 Xhat=np.dot(pca.transform(X)[:,:],pca.components_[:,:])

 Xhat+=X_meaned

 print(Xhat)

 print(pca.transform(X))

 print((pca.transform(X)).shape)

 print(pca.components_[:,:])
