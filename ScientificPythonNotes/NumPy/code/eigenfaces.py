import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_lfw_people

def run(numpca=150):

 faces = fetch_lfw_people(min_faces_per_person=60)
 print(faces.target_names)
 print(faces.images.shape)
 
 from sklearn.decomposition import PCA as RandomizedPCA
 pca = RandomizedPCA(numpca)
 pca.fit(faces.data)
 
 
 fig, axes = plt.subplots(3, 8, figsize=(9, 4),
                          subplot_kw={'xticks':[], 'yticks':[]},
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i, ax in enumerate(axes.flat):
     ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')
 

 plt.show()
 
 plt.plot(np.cumsum(pca.explained_variance_ratio_))
 plt.xlabel('number of components')
 plt.ylabel('cumulative explained variance');
 plt.show()
 
 
 
 # Compute the components and projected faces
 pca = RandomizedPCA(numpca).fit(faces.data)
 components = pca.transform(faces.data)
 projected = pca.inverse_transform(components)
 
 # Plot the results
 fig, ax = plt.subplots(2, 10, figsize=(10, 2.5),
                        subplot_kw={'xticks':[], 'yticks':[]},
                        gridspec_kw=dict(hspace=0.1, wspace=0.1))
 for i in range(10):
     ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
     ax[1, i].imshow(projected[i].reshape(62, 47), cmap='binary_r')
     
 ax[0, 0].set_ylabel('full-dim\ninput')
 ax[1, 0].set_ylabel(str(numpca)+'-dim\nreconstruction');

 plt.show()
