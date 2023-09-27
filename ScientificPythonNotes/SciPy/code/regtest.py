import numpy as np
from scipy.ndimage import shift
from astropy.io import fits


def run():


 image1=fits.open('../files/n0001e.fits')[0].data
 image2=fits.open('../files/n0024e.fits')[0].data

 image1=np.where(np.isnan(image1),0,image1)
 image2=np.where(np.isnan(image2),0,image2)

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

#write the difference between the first file and results from a more optimized code

 comparison_1=fits.open('../files/n0001reg.fits')[0].data
 
 difference=result1-comparison_1
 fits.writeto('../files/difference_1.fits',difference,overwrite=True)

 absreldiff=np.abs(difference)/comparison_1

 fits.writeto('../files/absreldiff.fits',absreldiff,overwrite=True)

