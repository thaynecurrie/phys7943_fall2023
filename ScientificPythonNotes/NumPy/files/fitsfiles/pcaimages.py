
from astropy.io import fits
import numpy as np
import glob
import matplotlib.pyplot as plt

def run(npca=8):

 filelist=glob.glob("*fits")

 test=fits.open(filelist[0])[0].data
 print(test.shape)
 print(len(filelist))

 imageset=np.zeros((len(filelist),test.shape[0]*test.shape[1]))
 #print(imageset.shape)

 #building image set

 imean=np.zeros(len(filelist))
 for i in range(len(filelist)):
 
  image=fits.open(filelist[i])[0].data
 
  bad=np.where(~np.isfinite(image))
  image[bad]=np.random.rand(1)

  imean[i]=np.mean(image.flatten())
  imageset[i,:]=image.flatten()-np.mean(image.flatten())

 
 #perform PCA

 cov=np.matmul(imageset,imageset.T)
 print(cov.shape)
 
 

 eig_val,eig_vec=np.linalg.eigh(cov)

 indices=np.argsort(eig_val)[::-1]
 eig_val=eig_val[indices]
 eig_vec=eig_vec[indices]

 eig_vec=eig_vec[:,:npca]
 eig_val=eig_val[:npca]

 pca_components=((imageset.T).dot(eig_vec)).T

 pca_images=pca_components.reshape(npca,test.shape[0],test.shape[1])

 print(pca_components.shape)
 print(pca_images.shape)

 
 fig, axes = plt.subplots(2, 4, figsize=(18, 8),
                          subplot_kw={'xticks':[], 'yticks':[]},
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))

 
 for i, ax in enumerate(axes.flat):
     clims=np.nanpercentile(pca_images[i,:,:],[2,98])
     #clims=[-10000,10000]
     ax.imshow(pca_images[i,:,:], cmap='jet',clim=clims)
     #ax.imshow(pca_components_[i].reshape(62, 47), cmap='bone')
     #ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')


 plt.show()



  
