import numpy as np



def ex1():


 aaa=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]])

# aaa.np.random.rand(5,4)

#with np.linalg.svd

 aaa_inv=np.linalg.pinv(aaa)

 print("the NumPy-produced inverted matrix is \n")
 print(aaa_inv)

#manual version

 new = np.asarray(aaa) #not really needed but we are following the NumPy syntax

# wrap = getattr(aaa, "__array_prepare__", new.__array_wrap__) ### def not needed to demonstrate the point

 rcond=1e-15 #default value for pseudo-inverse
 rcond=np.asarray(rcond)
 new = new.conjugate()

#taking the SVD
 u,s,vt=np.linalg.svd(new,full_matrices=False)

 #print(u.shape,s.shape,vt.shape)
 cutoff = rcond[..., np.newaxis] * np.amax(s, axis=-1, keepdims=True)

 large = s > cutoff
 s = np.divide(1, s, where=large, out=s)
 s[~large] = 0

 s_version2=s[...,np.newaxis]

 right_matrix=np.multiply(s_version2,np.transpose(u))

 aaa_inv2=np.matmul(vt.T,right_matrix)

 print("the manually-produced inverted matrix is \n")
 print(aaa_inv2)

 print("the residuals are ...")
 print(aaa_inv2-aaa_inv)

def ex2(rcond=1e-15):

#newer array
 aaa=np.array([[1.1,2.2,3.3,4.4],[5.5,6.6,7.7,8.7],[9.98,10.1,11.11,12.12],[13,14,15,16],[17,18,19,20]])

#original array
 #aaa=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]) 

 aaa=aaa[:4,:] #chopping off last row, making a 4x4 matrix

#a straight inverse

 aaa_invreg=np.linalg.inv(aaa)

#with np.linalg.svd

 aaa_inv=np.linalg.pinv(aaa)

#manually

 new = np.asarray(aaa)
# wrap = getattr(aaa, "__array_prepare__", new.__array_wrap__)

#rcond is now pushed to a keyword

 rcond=np.asarray(rcond)
 new = new.conjugate()

#taking the SVD
 u,s,vt=np.linalg.svd(new,full_matrices=False)

 cutoff = rcond[..., np.newaxis] * np.amax(s, axis=-1, keepdims=True)

 #print('cutoff is',cutoff)
 #print('s is ',s)
 #print(rcond*s,rcond*np.amax(s,axis=-1,keepdims=True))

 large = s > cutoff
 s = np.divide(1, s, where=large, out=s)
 s[~large] = 0

 s_version2=s[...,np.newaxis]

 right_matrix=np.multiply(s_version2,np.transpose(u))

 aaa_inv2=np.matmul(vt.T,right_matrix)

 #print("the straightforward inverse yields")
 print(aaa_invreg)

 #print("the NumPy pseudo-inverse yields")
 print(aaa_inv)

 #print("the manual pseudo-inverse yields")
 print(aaa_inv2)

 print("the difference between the straightforward inverse and NumPy pseudo-inverse are")
 print(np.max(aaa_invreg-aaa_inv))

 #print("difference bt manual and NumPy ",aaa_inv-aaa_inv2)

def ex3(rcond=1e-15):

 aaa=np.random.rand(91,91)
 
#a straight inverse

 aaa_invreg=np.linalg.inv(aaa)

#with np.linalg.svd

 aaa_inv=np.linalg.pinv(aaa,rcond=rcond)

#manually


 new = np.asarray(aaa)
# wrap = getattr(aaa, "__array_prepare__", new.__array_wrap__)

 #rcond=1e-15 #default value for pseudo-inverse
 #rcond=1e-5 #revised, test to see difference

 rcond=np.asarray(rcond)
 new = new.conjugate()

#taking the SVD
 u,s,vt=np.linalg.svd(new,full_matrices=False)

 #print(u.shape,s.shape,vt.shape)
 cutoff = rcond[..., np.newaxis] * np.amax(s, axis=-1, keepdims=True)

 #print('cutoff is',cutoff)
 #print('s is ',s)
 print(rcond*s,rcond*np.amax(s,axis=-1,keepdims=True))

 print(np.amax(s,axis=-1,keepdims=True))
 print(np.amin(s,axis=-1,keepdims=True))

 #plot stuff
 import matplotlib.pyplot as plt
 
 plt.plot(np.arange(0,len(s))+1,s/np.max(s),c='tab:green',marker='o',ms=2)
 plt.yscale('log')
 plt.ylim(np.min(s)/np.max(s),1.01)
 plt.xlabel('Singular Value',size=16)
 plt.ylabel('$\Sigma_{i}/\Sigma_{i,max}$',size=16)
 plt.show()
 

 large = s > cutoff

 print('truncated s is',s[large])

 s = np.divide(1, s, where=large, out=s)
 s[~large] = 0

 s_version2=s[...,np.newaxis]


 right_matrix=np.multiply(s_version2,np.transpose(u))

 #right_matrix.shape
 #(4,5)

 aaa_inv2=np.matmul(vt.T,right_matrix)

 #print("the straightforward inverse yields")
 #print(aaa_invreg)

 #print("the NumPy pseudo-inverse yields")
 #print(aaa_inv)

 #print("the manual pseudo-inverse yields")
 #print(aaa_inv2)

 print("the residual between the straightforward inverse and NumPy pseudo-inverse are")
 print(aaa_invreg-aaa_inv)
 print("the sigma-sum is ...")
 print(np.sum(((aaa_invreg-aaa_inv)**2.)))

 #print("difference bt manual and NumPy ",aaa_inv-aaa_inv2)

 print(np.linalg.cond(aaa))

