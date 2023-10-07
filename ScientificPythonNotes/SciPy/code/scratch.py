import numpy as np
from scipy import ndimage
from scipy.ndimage import shift
from astropy.io import fits

#from reg.charis_register_cube import shift_sub
from subroutines.interpolate_new import interpolate

def run():


 image1=fits.open('../files/n0001e.fits')[0].data
 image2=fits.open('../files/n0024e.fits')[0].data


 image1=np.where(np.isnan(image1),0,image1)
 image2=np.where(np.isnan(image2),0,image2)

 image1f=image1.copy()
 image2f=image2.copy()

 xcen,ycen=image1.shape[1]//2,image1.shape[0]//2
 print(xcen,ycen)

 #centroid1=[220.975,251.130]
 centroid1=[250.975,251.130]
 centroid2=[250.112,251.806]

 result1=shift(image1,(-centroid1[0]+ycen,-centroid1[1]+xcen),order=3)
 result2=shift(image2,(-centroid2[0]+ycen,-centroid2[1]+xcen),order=3)
 #result1=shift(image1,[centroid1[0]-ycen,centroid1[1]-xcen],order=3)
 #result2=shift(image2,[centroid2[0]-ycen,centroid2[1]-xcen],order=3)

 fits.writeto('../files/shifted_1.fits',result1,overwrite=True)
 fits.writeto('../files/shifted_2.fits',result2,overwrite=True)

 print(centroid1[0]-ycen,centroid1[0],ycen)
 result1b=shift_sub(image1f,-1*(centroid1[1]-xcen),-1*(centroid1[0]-ycen)).reshape(image1.shape[0],image1.shape[1])
 result2b=shift_sub(image2f,np.array(-centroid2[1]+xcen),np.array(-centroid2[0]+ycen)).reshape(image2.shape[0],image2.shape[1])

 #result1b=shift_sub(image1,np.array(-centroid1[1]+xcen),np.array(-centroid1[0]+ycen)).reshape(image1.shape[1],image1.shape[0])
 #result2b=shift_sub(image2,np.array(-centroid2[1]+xcen),np.array(-centroid2[0]+ycen)).reshape(image2.shape[1],image2.shape[0])
 #result1b=shift_sub(image1,np.array(+centroid1[1]-xcen),np.array(+centroid1[0]-ycen)).reshape(image1.shape[1],image1.shape[0])
 #result2b=shift_sub(image2,np.array(+centroid2[1]-xcen),np.array(+centroid2[0]-ycen)).reshape(image2.shape[1],image2.shape[0])

 print(result1b.shape)
 fits.writeto('../files/shifted_1b.fits',result1b,overwrite=True)
 fits.writeto('../files/shifted_2b.fits',result2b,overwrite=True)

def shift_sub(image, x0, y0, missing=np.nan):
    #shift image
#    if ((x0.astype(int) - x0) ==0) and ((y0.astype(int) - y0) ==0):
#        return np.roll(image, (int(y0), int(x0)), axis = (0,1))
    
    s = image.shape
    x = np.outer(np.ones(s[0]), np.arange(s[1]))
    y = np.outer(np.arange(s[0]), np.ones(s[1]))
    x1 = x-x0
    y1 = y-y0
    
    x1 = np.clip(x1, a_min = 0, a_max = s[1]-1.)
    y1 = np.clip(y1, a_min = 0, a_max = s[0]-1.)

#    return interpolate(image, y1.flatten(), x1.flatten(), cubic=-0.5, missing=missing)
    return ndimage.map_coordinates(image, [y1, x1], order=3)
