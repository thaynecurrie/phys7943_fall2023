import numpy as np

import matplotlib.pyplot as plt
from matplotlib.image import imread
plt.rcParams['figure.figsize']=[16,8]

def truncate_image(k=5):

 A=imread('thephoto.jpg')

 X=np.mean(A,-1)

 img=plt.imshow(X)
 img.set_cmap('gray')
 plt.axis('off')

 plt.show()

 U,s,VT=np.linalg.svd(X,full_matrices=False)
 Sigma=np.diag(s)


 X_Ap = np.dot(U[:,:k],Sigma[0:k,:k]).dot(VT[:k,:])

 img=plt.imshow(X_Ap)

 img.set_cmap('gray')
 plt.axis('off')
 plt.title('k = '+str(k))
 plt.show()
  #plt.savefig('hubble'+str(k)+'.png')


def denoise_image(k=5,nlevel=0.05,plotme=True):

 A=imread('cat.jpeg')

 A=sp_noise(A,nlevel)
 X=np.mean(A,-1)

 img=plt.imshow(X)
 img.set_cmap('gray')
 plt.axis('off')

 plt.show()

 U,s,VT=np.linalg.svd(X,full_matrices=False)
 Sigma=np.diag(s)

 if plotme:
  plt.plot(np.arange(0,len(s))+1,s/np.max(s),c='tab:green',marker='o',ms=2)
  plt.yscale('log')
  plt.ylim(np.min(s)/np.max(s),1.01)
  plt.xlabel('Singular Value',size=16)
  plt.ylabel('$\Sigma_{i}/\Sigma_{i,max}$',size=16)
  plt.show()


 X_Ap = np.dot(U[:,:k],Sigma[0:k,:k]).dot(VT[:k,:])

 img=plt.imshow(X_Ap)

 img.set_cmap('gray')
 plt.axis('off')
 plt.title('k = '+str(k))
 plt.show()
  #plt.savefig('hubble'+str(k)+'.png')


def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = image.copy()
    if len(image.shape) == 2:
        black = 0
        white = 255            
    else:
        colorspace = image.shape[2]
        if colorspace == 3:  # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([255, 255, 255], dtype='uint8')
        else:  # RGBA
            black = np.array([0, 0, 0, 255], dtype='uint8')
            white = np.array([255, 255, 255, 255], dtype='uint8')
    probs = np.random.random(output.shape[:2])
    output[probs < (prob / 2)] = black
    output[probs > 1 - (prob / 2)] = white
    return output
  
